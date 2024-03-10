# 100 days of coding - Python
# Day 10: Simple Calculator
# By Felipe Rojas
# Creating a simple calculator using functions
# The calculator will be able to do the following operations:
# addition, subtraction, multiplication, division
# Using a dictionary to store the operations and the functions

from art import logo

print(logo)
print("Python Calculator by Felipe Rojas")


# Addition operation
def add(n1, n2):
    return n1 + n2


# Substraction operation
def sub(n1, n2):
    return n1 - n2


# Multiplication operation
def mult(n1, n2):
    return n1 * n2


# Division operation
def div(n1, n2):
    return n1 / n2


def calculator():
    keep_calc = True

    operation = {
        '+': add,
        '-': sub,
        '*': mult,
        '/': div
    }
    first_num = int(input("Enter the first number: "))
    while keep_calc:
        selected_op = input("Which operation? (+, -, *, /): ")
        second_num = int(input("Enter the next number: "))

        '''
        if selected_op == '+':
            result = add(first_num, second_num)
            print(f"the result of {first_num} {selected_op} {second_num} is {result}")
    
        elif selected_op == '-':
            result = subs(first_num, second_num)
            print(f"the result of {first_num} {selected_op} {second_num} is {result}")
        
        elif selected_op == '*':
            result = mult(first_num, second_num)
            print(f"the result of {first_num} {selected_op} {second_num} is {result}")
        
        elif selected_op == '/':
            if second_num == 0:
                print("Cannot divide by 0")
            else:
                result = round(div(first_num, second_num), 2)
                print(f"the result of {first_num} {selected_op} {second_num} is {result}")
        
        else:
            print("Not a valid option")
        '''
        if selected_op == '/' and second_num == 0:
            print("Cannot divide by 0")
            calculator()
            keep_calc = False

        else:
            calc_function = operation[selected_op]
            result = calc_function(first_num, second_num)
            print(f"the result of {first_num} {selected_op} {second_num} is {result}")

            user_continue = input("Do you want to do other calculation? (y or n): ")

            if user_continue == 'n':
                keep_calc = False

                new_calc = input("Do you want to do a new calculation? (y or n): ")
                if new_calc == 'y':
                    calculator()
                else:
                    print("Thanks for using the Calculator")

            else:
                first_num = result
                print("Let's continue")


calculator()
