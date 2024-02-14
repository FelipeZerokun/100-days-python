# Day one project. Band name generator.
# Understanding Python variables and input function.
# input will get data from the user in the form of a string.
# Strings can be added together to get a new string variable.

print("Band name Generator, by Felipe Rojas")
# Ask the user for the city that they grew up in.
city = input("Enter the city where you grew up in: ")
# Ask the user for the name of a pet.
pet = input("enter the name of a pet: ")
# Combine the name of their city and pet and show them their band name.
band_name = city + pet
print(band_name)
# Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/