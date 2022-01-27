# Workout tracking app by Felipe Rojas

import requests
import os
from datetime import datetime

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
# print(result)
user_activity_name = result['exercises'][0]['name']
user_activity_duration = result['exercises'][0]['duration_min']
user_calories_burned = result['exercises'][0]['nf_calories']

print(f"The user did {user_activity_name} for {user_activity_duration} minutes and burned {user_calories_burned} kcal")