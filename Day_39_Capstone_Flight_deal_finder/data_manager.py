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

    def update_sheety_data(self, flight_obj, city_code, city_id):
        new_data = {
            "price": {
                "iataCode": city_code,
                "lowestPrice": flight_obj.price
            }
        }
        response = requests.put(url=f"{self.sheety_endpoint}/{city_id}",
                                headers=self.sheety_header,
                                json=new_data
        )
        print(response.text)

