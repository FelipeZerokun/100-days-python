with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file: # W to overwrite everything in the file
    file.write("New Text.")

with open("my_file.txt", mode="a") as file: # a to append new text to the file
    file.write("\nAdded Text.")

with open("created_file.txt", mode="w") as new_file:
    new_file.write("Open with mode 'w' creates a file in case there is no file in the directory")

