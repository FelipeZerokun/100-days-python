import requests
import os
from twilio.rest import Client

# Setting the variables for our APIs
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# Variables for the Twilio API
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

## Get stocks data from https://www.alphavantage.co
# Variables for the Stock API
stocks_api_key = os.environ['ALPHAVANTAGE_API_KEY']
url = f'https://www.alphavantage.co/query'
stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': stocks_api_key
}

## Get news from https://newsapi.org/
news_api = os.environ['NEWSAPI_API_KEY']
news_url = 'https://newsapi.org/v2/everything'
news_params = {
    'qInTitle': COMPANY_NAME,
    'apiKey': news_api
}


#TODO 1. - Get yesterday's closing pricee
r = requests.get(url, params= stock_params)
stocks_data = r.json()['Time Series (Daily)']
# print(data)
data_list = [value for (key, value) in stocks_data.items()] # Each item in the list is a day
# print(data_list)
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])
# print(yesterday_closing_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
dby_closing_price = float(day_before_yesterday_data['4. close'])
# print(dby_closing_price)

#TODO 3. - Find the positive difference between 1 and 2.
stock_status = ""
stock_price_difference = float(yesterday_closing_price - dby_closing_price)
if stock_price_difference < 0:
    stock_status = "🔻"
    stock_price_difference = abs(stock_price_difference)
else:
    stock_status = "🔺"

# print(stock_price_difference)

#TODO 4. - Work out the value of 5% of yesterday's closing price
diff_percentage = round((stock_price_difference/yesterday_closing_price)*100)
# print(diff_percentage)

#TODO 5. - If TODO4 is True the print("Get news) -> Later, instead of printing something, get the actual news


if diff_percentage > 5:
    print("Get News")
    r2 = requests.get(news_url, params=news_params)
    news_data = r2.json()['articles']
    # print(news_data)

    #TODO 6. - Use python slice operator to create a list that contains the first 3 articles
    three_articles = news_data[:3]
    # print(three_articles[0]['title'])
    #TODO 7. - Create a new list of the first 3 Articles headlines and description using list comprehensioin
    article_list = [f"Headline: {item['title']}. \nBrief: {item['description']}" for item in three_articles]
    # print(article_list)

    #TODO 8. - Send each article as a separated message via Twilio
    for article in article_list:
        # print(article)
        message = client.messages \
            .create(
                body=f"{STOCK}: {stock_status}{stock_price_difference}% \n{article}. ",
                from_='+13345649974',
                to='+593 99 787 9292'
        )

    #Optional: Format the SMS message like this:
    """
    TSLA: 🔺2%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    or
    "TSLA: 🔻5%
    Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
    Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
    """
