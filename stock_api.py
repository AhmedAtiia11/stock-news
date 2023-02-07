import requests
import os


STOCK = "TSLA"

STOCK_API_KEY=os.environ.get("STOCK_API_KEY")
stock_api_parameters={"function":"TIME_SERIES_DAILY_ADJUSTED","symbol":STOCK,"apikey":STOCK_API_KEY}
stock_response=requests.get("https://www.alphavantage.co/query",params=stock_api_parameters)
