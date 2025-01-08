import requests
from twilio.rest import Client
import secrets

STOCK = "DIS"
COMPANY_NAME = "Walt Disney Co."

parameters_stocks = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": secrets.STOCKS_KEY,
}

# parameters_stocks = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": "IBM",
#     "apikey": "demo",
# }

parameters_news = {
    "q": secrets.COMPANY_NAME,
    "searchIn": "title",
    "sortBy": "popularity",
    "apiKey": secrets.NEWS_KEY,
}

stocks_response = requests.get(url="https://www.alphavantage.co/query", params=parameters_stocks)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()["Time Series (Daily)"]

stocks_data_list = [value for (key, value) in stocks_data.items()]

yesterday = stocks_data_list[0]
close_yesterday = float(yesterday["4. close"])
before_yesterday = stocks_data_list[1]
close_before_yesterday = float(before_yesterday["4. close"])

exchange_stock = round(((close_yesterday - close_before_yesterday) * 100 / close_before_yesterday), 2)


def raise_or_down():
    if exchange_stock >= 0:
        return f"{STOCK} +{abs(exchange_stock)}%"
    else:
        return f"{STOCK} -{abs(exchange_stock)}%"


if abs(exchange_stock) >= 1:
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news_data_list = news_data[:3]

    formatted_articles = []

    for article in news_data_list:
        item = f"{raise_or_down()}\nHeading: {article["title"]}\nBrief: {article["description"]}\nlink: {article["url"]}\n"
        formatted_articles.append(item)

    # formatted_articles = [(f"{raise_or_down()}\nHeading: {article["title"]}\nBrief: {article["description"]}\nlink: "
    #                        f"{article["url"]}\n") for article in news_data_list]

    for article in formatted_articles:
        client = Client(secrets.ACCOUNT_SID, secrets.AUTH_TOKEN)
        message = client.messages.create(
            body=article,
            from_=secrets.TWILIO_NUMBER,
            to=secrets.MY_NUMBER,
        )
