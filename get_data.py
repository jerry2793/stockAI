from requests import get
from datetime import datetime


def historical_save_gen(json):
    # generates rows in the correct (corresponding) format to save
    for i in range(len(json['t'])):
        row = []
        # print('main loop')
        for k in json.keys():
            print(k)
            if k == 's':
                continue
            else: 
                # print('continued')
                row.append(list(json[k])[i])
                # print(k)
        yield row


def save(r):
    # saves the row
    pass


def getHistoricalData(s,start,finish,res=1):
    '''
    params: 
    s: symbol (stock) of desire (str),
    start: (unix timestamp) date from (1572651390),
    finish: (unix timestamp) date to (1572910590),
    res: the resolution of the data
    '''
    params = {
        'symbol': s,
        'resolution': res,
        'from': start,
        'to': finish,
        'token': 'btbetpn48v6tim9d4ve0'
    }
    url = 'http://finnhub.io/api/v1/stock/candle'
    r = get(url,params=params)

    return dict(r.json())


def main():
    r = getHistoricalData(
                'AAPL',
                datetime(2020,9,9).timestamp(),
                datetime(2020,9,8).timestamp()
                )
    # print(r)
    # j = 0
    for i in historical_save_gen(r):
        # print(i)

        save(i)

        # j += 1
        # if j == 10: 
        #     break
        # break


if __name__ == '__main__':
    main()