import requests
import os


COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
news_api_parameters={"q":COMPANY_NAME,"apikey":NEWS_API_KEY}
news_response=requests.get("https://newsapi.org/v2/everything",params=news_api_parameters)
