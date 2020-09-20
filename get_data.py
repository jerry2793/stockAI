from requests import get
from datetime import datetime, timedelta 
import sqlite3

# all you need to do is to change the STOCKS with appr symbols conn = sqlite3.connect('data.db') c = conn.cursor() KEYS = ['c','h','l','o','t','v'] STOCKS = ['aapl','AMZN'.lower(),'NVDA'.lower()]
for i in STOCKS:
    try:
        print(f'creating table: {i}')
        c.execute(f"""CREATE TABLE {i} (
            c real,
            h real,
            l real,
            o real,
            t real,
            v real
        )""")
    except:
        pass

def historical_save_gen(json):
    # generates rows in the correct (corresponding) format to save
    # print(json)
    for i in range(len(json['t'])):
        row = []
        # print('main loop')
        # print(json.keys())
        for k in json.keys():
            # print(k)
            if k == 's':
                continue
            else:
                # print('continued')
                row.append(list(json[k])[i])
                # print(k)
        yield row


def save(r):
    # saves the row
    cols = ''
    for i in KEYS:
        cols += f'{i},'
    values = ''
    for i in r:
        values += f'{i},'
    c.execute(f"INSERT INTO aapl ({cols.strip(',')}) VALUES ({values.strip(',')})")


def getHistoricalData(s,start,finish,res=1):
    '''
    params:
    s: symbol (stock) of desire (str),
    start: (unix timestamp) date from (1572651390),
    finish: (unix timestamp) date to  (1572910590),
    res: the resolution of the data
    '''
    params = {
        'symbol': s,
        'resolution': res,
        'from': start,
        'to': finish,
        'token': 'btbetpn48v6tim9d4ve0'
    }
    url = 'https://urldefense.com/v3/__http://finnhub.io/api/v1/stock/candle__;!!I5pVk4LIGAfnvw!x6oGMmHXru6nL2xgMlJI0A7DCuC2Pxwxm1ZodRd35F7WGpUyVK6S6GtOmLiGwn8y6zCM$ '
    r = get(url,params=params)
    # print(r.status_code)

    return dict(r.json())


def date_gen(start,finish):
    '''
    example:
    start: 2019,5,6
    finish: 2020,4,8
    returns: timestamp of start (earlier) to finish (later)
    '''
    x = finish - start
    for i in range(x.days):
        s = finish - timedelta(days=i)
        f = finish - timedelta(days=i-1)
        yield [s.timestamp(),f.timestamp()]


def main(q,start,finish):
    r = getHistoricalData(
                q.upper(),
                start,
                finish
                )
    # print(r)
    # j = 0
    for i in historical_save_gen(r):
        # print(i)

        save(i)
        print(i)
        # j += 1
        # if j == 10:
        #     break
        # break


if __name__ == '__main__':
    for i in STOCKS:
        print(i.upper())
        for j in date_gen(datetime(2019,9,17),datetime(2020,8,30)):
            # print(j)
            main(i.upper(),j[0],j[1])


    # for i in date_gen(datetime(2020,7,5),datetime(2020,8,6)):
    #     print(str(i))


        conn.commit()
    conn.close()
