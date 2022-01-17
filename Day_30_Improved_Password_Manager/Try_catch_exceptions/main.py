# Kind of errors in Python

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key":"value"}
# a_dictionary["another_key"]

# IndexError
# fruit_list = ["apple", "pear", "orange"]
# fruit = fruit_list[3]

# #TypeError
# print(3+"b")

##################################### CATCHING ERRORS #####################################
# try:
#     file = open("a_file.txt")
#     #a_dictionary = {"key":"value"}
#     #print(a_dictionary["another_key"])
#
# except FileNotFoundError:
#     # File not found, creating the file instead
#     open("a_file.txt", "w")
#     file.write("something \n")
#
# except KeyError as error_message:
#     print(f"Error in Key: {error_message}")
#
# else:
#     print("Everything was successful!")
#
# finally:
#     print("With or without errors, this will be printed")
#     file.close()
#
#     # But If I want to raise an exception on my own:
#     raise TypeError("This is an error that I made up")


# Example

# height = float(input("Enter your height (cm): "))
# weight = int(input("Enter your weight (kg): "))
#
# # Let's raise an excepction if the height is unrealistic
# if height > 250:
#     raise ValueError("Humans can't be that tall!")
#
# bmi = weight / height**2
# print(bmi)

# Challenge
# Fix an IndexError
# fruits = ["Apple", "Pear", "Orange"]
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Not a valid option!")
#     else:
#         print(fruit + " pie")
#
# user_input = int(input("Enter a number between 0 and 4: "))
# make_pie(user_input)

# Challenge 2
facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3}

]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post["Likes"]
    except KeyError:
        print("Posts with no likes :( ")

print(total_likes)