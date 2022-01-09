# 100 Days of Python
## Project 13: Debugging Exercise

This is not a project itself, but rather a debuggin practice.

In this project are three flies, each has a small code that has one problem. The goal of this project is to review each code and find the bug preventing it from working like intended.

In the first file, debug_01, the code should take a integer number as input and return a text saying if the number is even or odd.
The problem with the code is that it tries to compare two values with the assignation sign ("=" is for assignation, "==" is for comparison). This is a SyntaxError.
So, instead of this -> if number % 2 = 0:, you should write this -> if number % 2 == 0:

If you run this file with a debugger, it will show a message like this: "SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?"
Also, in Pycharm and other IDEs, even before you run the code the IDE will mark the mistake with a red underline.

For the second file, the code will take a year from the user, and return in text if it is a leap year or not.
Here you will not see the error before running like in the exercise number one, because there is no actual error in the code. But if you try to run the code the following message will be shown: "TypeError: not all arguments converted during string formatting". The TypeError means that we are trying to associate two different types of variables. In this case, strings with integers. Remember that the "input" method give us a variable in the form of string. So, if we want to use it as a integer, float or any kinf of number we must convert it first. year = int(input("Which year do you want to check?")) the int method here should do the trick.

For the third file, 


