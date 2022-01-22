import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# API endpoint from https://openweathermap.org
# using a free subscription to ONE call API https://openweathermap.org/api/one-call-api
# My twilio recovery code: Td6JqqtCAsEzXClvVoBx7dNT1iEX_yx3wALjRlJ2

API_KEY = 'd7de006bb161c943ebbea55409fb01d3'
ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    "lat": -0.096190,
    "lon": -78.470730,
    "appid": 'd7de006bb161c943ebbea55409fb01d3',
    "exclude": 'current,minutely,daily',
    "units": 'metric'
}

twilio_account_sid = 'AC3b89cc2650bfd0cfa8dc8c61c956dfe5'
twilio_auth_token = 'f8e44afccb63027df521116a99852635'
my_twilio_num = '+13345649974'

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
        to='+593997879292'
    )
    print(message.status)
