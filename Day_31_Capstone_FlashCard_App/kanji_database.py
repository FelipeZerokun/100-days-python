import json
import pandas as pd

with open("data/kanji-kyouiku.json", encoding="utf8") as kanji_file:
    kanji_dataset = json.load(kanji_file)


try:
    user_list = []
    csv_data = pd.read_csv("data/kanjis_to_learn.csv", index_col=0)
    csv_data = csv_data.values.tolist()
    print("there is data")
    for kanji in csv_data:
        # print(kanji[0])
        user_list.append(kanji[0])




except:
    user_list = []
    for (key, value) in kanji_dataset.items():
        user_list.append(key)
    new_dataframe = pd.DataFrame(user_list)
    new_dataframe.to_csv("data/kanjis_to_learn.csv")
    print("no data")

# print(user_list)