import datetime as dt
import os
from twilio.rest import Client
from stock_api import stock_response
from news_api import news_response

#---------------------------Parameters Decleration------------------------#

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

#---------------------Yesterday Closing Price Calculations----------------#

yesterday = dt.datetime.now() - dt.timedelta(days=1)
yesterday=str(yesterday).split(" ")[0]
stock_data=stock_response.json()["Time Series (Daily)"]
yesterday_closing_price=float(stock_data[yesterday]["4. close"])
print(f"Yesterday_closing_price: {yesterday_closing_price}")

#----------------------Day Before Closing Price-----------------------------#

day_before_yesterday_list=[value for (key,value) in stock_data.items()]
day_before_yesterday_price=float(day_before_yesterday_list[1]["4. close"])
print(f"The_Day_before_yesterday_price: {day_before_yesterday_price}")

#-------Difference Between Yesterday's price and the day before price--------#

difference=abs(yesterday_closing_price-day_before_yesterday_price)
percentage_difference=(difference*100)/yesterday_closing_price
print(f"The difference: {difference}")
print(f"The percentage: {percentage_difference}%")

#-----Sent news related to Company Stock to user if percentage exceed 2%-------#
if percentage_difference > 2:
    print(f"--------Sent News related to {COMPANY_NAME} Stock-------")
    news_articles=news_response.json()["articles"][:3]
    msg_to_sent=[f"Title: {article['title']} , Description: {article['description']}" for article in news_articles]
    account_sid = os.environ.get("account_sid")
    auth_token = os.environ["auth_token"]
    client = Client(account_sid, auth_token)
    for article in msg_to_sent:
        message = client.messages.create(
        body=f"{article}",
        from_="",
        to=""
        )    


