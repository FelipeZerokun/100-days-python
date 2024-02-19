# 100 days of coding - Python
# Day 2: Tip Calculator
# By Felipe Rojas
# Learning how to use numeric variables with the input function.
# Changing variables data types with the int() and float() functions.

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to tip Calculator")
bill  = float(input("What was the total of the bill?: $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12, or 15?: "))
num_ppl = int(input("How many people to split the bill?: "))

individual_payment = round((bill/num_ppl)*(1+(tip_percent/100)), 2)
print(f"Each person should pay ${individual_payment}")