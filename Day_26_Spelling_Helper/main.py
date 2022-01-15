import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}
# print(nato_dict)

success_input = False
while not success_input:
    user_name = input("Enter a name to spell: ").upper()
    try:
        nato_name_list = [nato_dict[letter] for letter in user_name]

    except KeyError:
        print("Only letters are accepted!")

    else:
        print(nato_name_list)
        success_input = True
