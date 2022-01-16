# 100 Days of Python
## Project 26: Spelling helper project

This project is a tool for spelling. The user enters a Name, and using the nato phonetic alphabet, the program will spell that name letter by letter.

In this project I will practising a bit dictionary and list comprehension. 
This is really useful for when we need to use specific parts of a list or a dictionary. For example, in the previous project we needed only the squirrels with specific fur color. With a condictional, que took only the columns that met that condition.

Dictonary comprehension: new_dict = {new_key:new_value for item in list}
List comprehension: new_list = new_item for item in list if test

Using read_csv from Pandas library, I imported a csv file with the nato alphabet as a DataFrame.Then I used dictionary comprehension to convert the data in this DataFrame to a list, where the keys will be the letters in the alphabet and the values will be the phonetic equivalent to each letter. 

So far, when an error ocurred during the code execution, we let the debugger catch it but this would stop the program. Sometimes, this error is not our fault. For example, in the calculator project we ask the user to enter a number, but the user can makesa mistake and enter a letter. If I try to convert a letter to a integer number, there will be an error and the program will end. We can avoid this by using Exception Handling. With the keyword Try we can try lines of codes that may incur into an error, and print a message instead of completely stopping the code.
We will start using Exception handling to avoid ending the code abruptly, and give the user another chance to enter the correct information. In this case, the user must enter only alphabetic characters. If the user enters a number, with Try I will catch that error, and print a message for the user. Inside of a While loop, I will keep looping until the user enters a valid input.
I could use a for loop to check letter by letter the name the user entered as input, but with list comprehension I can do the same in a simple line of code.
