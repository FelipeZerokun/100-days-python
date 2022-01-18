# 100 Days of Python
## Project 29: Password manager

This is a small APP project that let's the user manage all of his/hers passwords. In a previous project I made a random password generator, and I will implement the same code here.

The GUI will have three spaces for the user to enter the website, the email for that website and the password. The user will also have a button to randomly generate a password if needed.

I will be using the TKinter module. Also I imported some methods from the random module for the password generator.

I defined two functions. In the generate_password function I used almost the same code as the day 05 project. This code will return a random password with 5 to 7 letters, 2 to 5 numbers and 2 to 5 symbols.

The other function is save. This function will take all the information in the textboxs and wil save it in a file called data.txt. I used the open and write methods with the keywords "with" and "as" for this.

