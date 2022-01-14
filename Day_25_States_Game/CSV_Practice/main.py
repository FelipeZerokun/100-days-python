# with open("weather_data.csv") as weather:
#     data = weather.readlines()
# print(data)

# import csv
# temperatures_list = []
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     for row in data:
#         if row[1] != "temp":
#             temperatures_list.append(int(row[1]))
#
# # print(data)
# print(temperatures_list)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(data)
temperature_list = data["temp"]
# print(temperature_list)
# print(type(temperature_list))

# Panda Frame Conversion
data_dict = data.to_dict()
# print(data_dict)

# Panda Series conversion
temp_list = data["temp"].to_list()
# print(temp_list)
# print(type(temp_list))

# Panda Series Methods
# print(temperature_list.mean())
# print(temperature_list.max())

# Get data in Columns
# print(data["conditions"])
# print(data.temp)

# Get data in Rows
# print(data[data["day"] == "Monday"])

# Challenge. Get which day of the week had the highest temperature
# print(data[data["temp"] == data["temp"].max()])
# print(data[data.temp == data.temp.max()])

# Challenge. Get Monday temperature and convert it to Farenheit
monday = data[data["day"] == "Monday"]
monday_temp = monday.temp
# print(monday_temp)
monday_farenheit = monday_temp * 9 / 5 + 32
# print(monday_farenheit)

# Create a Dataframe from scratch
data_dict = {
    "students": ["Felipe", "Jorge", "Isa"],
    "scores": [100, 98, 75]
}
data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")