import json
import requests 
import yfinance as yf
from yahoo_fin import stock_info as si
import pymongo

def main(stock, startDate, endDate):

    data = yf.download("SPY "+stock, start=startDate, end=endDate)

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    stockdb = myclient["stockdb"]

    #collectionNames =  myclient["stockdb"].list_collection_names(session=None, filter=None)

    stockCol = stockdb[stock]  

    print(data.info)

    records = json.loads(data.to_json()).values()
    stockCol.insert(records)
    

main("AAPL", "2017-01-01", "2017-04-30")