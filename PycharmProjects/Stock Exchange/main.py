import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
paras = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": " FEVXCPP1WMDWFE28",
}
# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url="https://www.alphavantage.co/query?", params=paras)
data = response.json()["Time Series (Daily)"]
time = [float(value["4. close"]) for (key, value) in data.items()][:2]
# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
res = time[0] - time[1]
if res < 0:
    res *= -1
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
per = 0
is_inc = False
if time[0] > time[1]:
    per = round((res / time[0]) * 100, 2)
    is_inc = True
elif time[0] < time[1]:
    per = round((res / time[1]) * 100, 2)
# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if per > 5.0:
    news_paras = {
        "q": COMPANY_NAME,
        "from": "2023-07-19",
        "to": "2023-07-21",
        "apiKey": "8231e03107e44c33b2cafe1c0afb0743",
        "language": "en",
    }
    new_res = requests.get(url="https://newsapi.org/v2/everything", params=news_paras)
    dat = new_res.json()["articles"][:3]
    articles = [{"description": value["description"], "title": value["title"]} for value in dat]
    for article in articles:
        if is_inc:
            msg = f"""
            {STOCK_NAME}:🔺{per}%
            HeadLine:{article["title"]}
            Brief:{article["description"]}
            """
        else:
            msg = f"""
                    {STOCK_NAME}:🔻{per}%
                    HeadLine:{article["title"]}
                    Brief:{article["description"]}
                    """
        sid = "AC9842f3a9d9d780edf7a92b75bde0c4f0"
        aut_tok = "90f896cc2d026e464daec9ecc115483b"
        client = Client(sid, aut_tok)
        mesg = client.messages.create(body=msg, from_="+14323093892", to="+923135362340")
        print(mesg.status)
## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
