# 100 days of coding - Python
# Day 5: Password Generator.
# By Felipe Rojas
# Learning how to FOR loops and the random module to generate randome passwords.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
'''
pw_generated = ""
for letter in range(nr_letters):
  rnd_letter = random.randint(0, len(letters)-1)
  pw_generated += letters[rnd_letter]

for symbol in range(nr_symbols):
  rnd_symbol = random.randint(0, len(symbols)-1)
  pw_generated += symbols[rnd_symbol]

for symbol in range(nr_numbers):
  rnd_number = random.randint(0, len(numbers)-1)
  pw_generated += numbers[rnd_number]

print(pw_generated)
'''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random_characters = []
pw_generated = ""

total_chars = nr_letters + nr_symbols + nr_numbers
#First I want to create lists with all the random characters I will use in the final password
for letter in range(nr_letters):
  random_letter = letters[random.randint(0, len(letters)-1)]
  #print(random_letter)
  random_characters.append(random_letter)

for symbol in range(nr_symbols):
  random_symbol = symbols[random.randint(0, len(symbols)-1)]
  #print(random_symbol)
  random_characters.append(random_symbol)

for letter in range(nr_numbers):
  random_number = numbers[random.randint(0, len(numbers)-1)]
  #print(random_number)
  random_characters.append(random_number)

# Now, I will randomize the order of the characters in the password

for i in range(total_chars):
  #print(random_characters)
  random_char = random.randint(0, len(random_characters)-1)
  pw_generated += random_characters.pop(random_char)

print(pw_generated)