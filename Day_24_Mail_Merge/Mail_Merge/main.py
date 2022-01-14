#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name
#Save the letters in the folder "ReadyToSend"

PLACEHOLDER = "[name]"

with open("./Input/Names/invented_names.txt") as names:
    name_list = names.readlines()


with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    for name in name_list:
        name = name.strip()
        new_letter = starting_letter.replace("[name]", name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as n_letter:
            n_letter.write(new_letter)


# print(name_list)
# print(starting_letter)
