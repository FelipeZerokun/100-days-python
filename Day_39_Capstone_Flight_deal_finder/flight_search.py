import os
import requests
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.tequila_endpoint = "https://tequila-api.kiwi.com"
        self.tequila_api = os.environ['TEQUILA_API_KEY']

    def get_iata_codes(self, city_name):
        location_endpoint = f"{self.tequila_endpoint}/locations/query"
        headers = {"apikey": self.tequila_api}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def get_flights_data(self, from_city, to_city, from_date, to_date):
        headers = {"apikey": self.tequila_api}
        query = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": from_date,
            "date_to": to_date,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f"{self.tequila_endpoint}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
