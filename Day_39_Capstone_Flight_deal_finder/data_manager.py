import os
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.flights_data = {}
        self.sheety_endpoint = os.environ['SHEETY_ENDPOINT']
        self.sheety_header = {
            'Authorization': f'Bearer {os.environ["MY_SHEETY_TOKEN"]}'
        }


    def get_sheety_data(self):
        response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
        data = response.json()
        self.flights_data = data['prices']
        return self.flights_data
