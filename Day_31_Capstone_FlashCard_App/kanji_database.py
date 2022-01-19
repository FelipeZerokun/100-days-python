import json

with open("data/kanji-kyouiku.json", encoding="utf8") as kanji_file:
    kanji_dataset = json.load(kanji_file)

kanji_list = []

for (key, value) in kanji_dataset.items():
    kanji_list.append(key)

    # print(key)
