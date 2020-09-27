import json
import pandas as pd
from datetime import datetime
import pytz
import time

def getDailyStockWith5MinTimeframe(stock):
    API_KEY = '7XB7FJ1P3CCMSZNC'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + stock + '&interval=5min&apikey=' + API_KEY + '&datatype=csv'
    df = pd.read_csv(url)

    df.to_csv(stock + datetime.today().strftime('%Y-%m-%d') + '.csv')
    

while True:
    tz_NY = pytz.timezone('America/New_York') 
    datetime_NY = datetime.now(tz_NY)
    print(datetime_NY.second)
    if datetime_NY.hour == 14 and datetime_NY.minute == 0 and (datetime_NY.strftime("%A") == 'Monday' or datetime_NY.strftime("%A") == 'Tuesday' or datetime_NY.strftime("%A") == 'Wednesday' or datetime_NY.strftime("%A") == 'Thursday' or datetime_NY.strftime("%A") == 'Friday'):
        #if datetime_NY.strftime("%A") == 'Monday' or datetime_NY.strftime("%A") == 'Tuesday' or datetime_NY.strftime("%A") == 'Wednesday' or datetime_NY.strftime("%A") == 'Thursday' or datetime_NY.strftime("%A") == 'Friday':
        getDailyStockWith5MinTimeframe("AAPL")       
    else:
        print('Sleeping at ' + datetime.today().strftime('%Y-%m-%d-%H-%M-%S') + '. Press Ctrl \'C\' to exit program.')
        time.sleep(30)