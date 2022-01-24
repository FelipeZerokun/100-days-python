import os
import requests
from twilio.rest import Client

# API endpoint from https://openweathermap.org
# using a free subscription to ONE call API https://openweathermap.org/api/one-call-api

# First, I did the connection to OpenWeatherMaps.org
API_KEY = os.environ['WEATHER_API_KEY']
ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'

# Again, I used the website latlong.net to get my coords
weather_params = {
    "lat": -0.096190,
    "lon": -78.470730,
    "appid": API_KEY,
    "exclude": 'current,minutely,daily',
    "units": 'metric'
}

# Then, the variables for the Twilio connection
twilio_account_sid = os.environ['MY_TWILIO_ID']
twilio_auth_token = os.environ['MY_TWILIO_TOKEN']
my_twilio_num = os.environ['MY_TWILIO_NUMBER']

response = requests.get(ENDPOINT, params=weather_params)
hourly_data = response.json()["hourly"]
print(hourly_data)
weather_slice = hourly_data[:12]
will_rain = False
for hour_weather in weather_slice:
    condition_code = hour_weather["weather"][0]
    print(condition_code)
    if int(condition_code['id']) < 700:
        will_rain = True

if will_rain:
    print("It is going to rain !")
    my_twilio_client = Client(twilio_account_sid, twilio_auth_token)
    message = my_twilio_client.messages \
        .create(
        body="It is going to rain today. Bring an umbrella",
        from_=my_twilio_num,
        to='+593997879292'
    )
    print(message.status)
