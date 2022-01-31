#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

sheety_manager = DataManager()
flights_data = sheety_manager.get_sheety_data()
print(flights_data)
flight_search = FlightSearch()
notification_manager = NotificationManager()


starting_city = 'UIO'
tomorrow = datetime.now() + timedelta(days=1)
in_six_months = datetime.now() + timedelta(days=(6 * 30))

# First, check and update the IATA codes from the Spreadsheet
for city in flights_data:
    # First, I checked every IATA code.
    if city["iataCode"] == "":
        print(f"No IATA code for the city {city['city']}")
        city["iataCode"] = flight_search.get_iata_codes(city['city'])


    # print(flights_data)
    # Then, I used each IATA code to check the flight information
    flight = flight_search.get_flights_data(
        starting_city,
        city["iataCode"],
        tomorrow.strftime("%d/%m/%Y"),
        in_six_months.strftime("%d/%m/%Y")
    )
    if flight == None:
        pass

    elif flight.price < city["lowestPrice"]:
        print(f"Low price found for {flight.destination_city}!")
        sheety_manager.update_sheety_data(flight, city["iataCode"], city["id"])

        notification_manager.send_sms(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )




