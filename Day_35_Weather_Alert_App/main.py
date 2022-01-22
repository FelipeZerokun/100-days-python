import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# API endpoint from https://openweathermap.org
# using a free subscription to ONE call API https://openweathermap.org/api/one-call-api
# My twilio recovery code: Td6JqqtCAsEzXClvVoBx7dNT1iEX_yx3wALjRlJ2

API_KEY = 'YOUR_API_KEY'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    "lat": -0.096190,
    "lon": -78.470730,
    "appid": 'API_ID',
    "exclude": 'current,minutely,daily',
    "units": 'metric'
}

twilio_account_sid = 'USER_ID'
twilio_auth_token = 'SECRET_TOKEN'
my_twilio_num = 'TWILIO_NUM'

response = requests.get(ENDPOINT, params=weather_params)
hourly_data = response.json()["hourly"]
# print(hourly_data)
weather_slice = hourly_data[:12]
will_rain = False
for hour_weather in weather_slice:
    condition_code = hour_weather["weather"][0]
    print(condition_code)
    if int(condition_code['id']) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella !")
    my_twilio_client = Client(twilio_account_sid, twilio_auth_token, http_client=proxy_client)
    message = my_twilio_client.messages \
        .create(
        body="It is going to rain today!",
        from_=my_twilio_num,
        to='YOUR_NUMBER'
    )
    print(message.status)
