import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""

TWILIO_ACCOUNT_SID = ""
TWILIO_AUTH_TOKEN = ""

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
data_before_yesterday_data = data_list[1]
data_before_yesterday_closing_price = data_before_yesterday_data["4. close"]

# difference = abs(float(yesterday_closing_price) - float(data_before_yesterday_closing_price))

difference = float(yesterday_closing_price) - float(data_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percent)

if abs(diff_percent) > 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [(f" {STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['title']}. "
                           f"\nBrief: {article['description']}") for article in three_articles]
    print(formatted_articles)

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="",
            to="+919459111291"
        )
        print(message.status)
