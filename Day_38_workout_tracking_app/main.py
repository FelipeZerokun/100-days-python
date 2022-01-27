# Workout tracking app by Felipe Rojas

import requests
import os
from datetime import datetime

# My nutritionix variables
MY_NUTRI_ID = os.environ['NUTRI_ID']
MY_NUTRI_API_KEY = os.environ['NUTRI_API']
nutri_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

nutri_params = {
    "query": input("What did you do today?: "),
    "gender": "male",
    "weight_kg": 93.2,
    "height_cm": 174.7,
    "age": 28,
}

headers = {
    "x-app-id": MY_NUTRI_ID,
    "x-app-key": MY_NUTRI_API_KEY,
}

response = requests.post(nutri_endpoint, json=nutri_params, headers= headers)
result = response.json()

# Now, I need to send all this information to my Google Spreadsheet with Sheety
# My Sheety variables
MY_SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
sheety_endpoint = os.environ['SHEETY_ENDPOINT']
sheety_header = {
    "Authorization": f"Bearer {MY_SHEETY_TOKEN}"
}

for activities in result['exercises']:
    user_activity_name = activities['name']
    user_activity_duration = activities['duration_min']
    user_calories_burned = activities['nf_calories']
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.today().strftime("%H:%M:%S")
    # print(f"On the {date} at {time}, the user did {user_activity_name} for {user_activity_duration} minutes and burned {user_calories_burned} kcal")

    sheety_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": user_activity_name.title(),
            "duration": user_activity_duration,
            "calories": user_calories_burned
        }
    }
    sheet_response = requests.post(sheety_endpoint, json=sheety_inputs, headers=sheety_header)

    print(sheet_response.text)
