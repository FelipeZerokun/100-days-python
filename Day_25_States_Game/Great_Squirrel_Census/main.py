import pandas
import pandas as pd

data_file = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur_squirrels = data_file[data_file["Primary Fur Color"] == "Gray"]
num_gray = len(gray_fur_squirrels)

red_fur_squirrels = data_file[data_file["Primary Fur Color"] == "Cinnamon"]
num_red = len(red_fur_squirrels)

black_fur_squirrels = data_file[data_file["Primary Fur Color"] == "Black"]
num_black = len(black_fur_squirrels)

# print(num_black, num_red, num_gray)

# Lets make it a dictionary and then transform it into a series

fur_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray, num_red, num_black]
}
print(fur_dict)
df = pandas.DataFrame(fur_dict)
df.to_csv("squirrel_count.csv")