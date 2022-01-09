from menu import coffees
#from replit import clear

# TODO 1. Create the variables for the coffee machine
money = {
    "pennies": 0,
    "nickles": 0,
    "dimes": 0,
    "quarters": 0
}
ingredients = {
    "water": 100,
    "milk": 750,
    "coffee": 100,
}
on_state = True


# TODO 2. Create a small function to count all the coins and return the total


def money_count(quarters, dimes, nickles, pennies):
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


#  TODO 3. Create the loop and the variables for ingredients, money and on/off state of the machine


while on_state:
    # Prompt for the user to pick from the menu
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # print(f"You picked {user_choice}")

    # TODO Create a word check for incorrect inputs
    if user_choice == 'espresso' or user_choice == 'cappuccino' or user_choice == 'latte':
        print(f'It has a cost of {coffees[user_choice]["cost"]}')
        print("Please, insert coins")
        user_quarters = int(input("How many quarters?: "))
        user_dimes = int(input("How many dimes?: "))
        user_nickles = int(input("How many nickles?: "))
        user_pennies = int(input("How many pennies?: "))
        user_money = money_count(user_quarters, user_dimes, user_nickles, user_pennies)
        # TODO check if the money the user inserted is enough (using the function created above)
        if user_money < coffees[user_choice]["cost"]:
            #clear()
            print("Not enough money. You'll have a total refund")
        # TODO Also, need to check if there are enough ingredients to prepare the coffee
        elif ingredients["water"] < coffees[user_choice]["ingredients"]["water"] or ingredients["milk"] < \
                coffees[user_choice]["ingredients"]["milk"] or ingredients["coffee"] < \
                coffees[user_choice]["ingredients"]["coffee"]:
            print("Sorry, not enough ingredients. You'll have a total refund")
        else:
            #clear()
            print("Preparing your coffee... Please wait...")
            money['quarters'] += user_quarters
            money['nickles'] += user_nickles
            money['dimes'] += user_dimes
            money['pennies'] += user_pennies
            ingredients["water"] -= coffees[user_choice]["ingredients"]["water"]
            ingredients["milk"] -= coffees[user_choice]["ingredients"]["milk"]
            ingredients["coffee"] -= coffees[user_choice]["ingredients"]["coffee"]
            print(f"Enjoy your {user_choice}!")

    # TODO Finally, add the other options for the machine technicians :P

    elif user_choice == 'report':
        total_money = money_count(money['quarters'],
                                  money['dimes'],
                                  money['nickles'],
                                  money['pennies'])
        print("Current ingredients are: ")
        print(f"Water: {ingredients['water']} ml")
        print(f"Milk: {ingredients['milk']} ml")
        print(f"Coffee: {ingredients['coffee']} g")
        print(f"Money in the machine: {total_money}")
        go_back = input("To go back enter any input: ")
        #clear()
    elif user_choice == 'off':
        on_state = False
        print("Thanks for using the coffee Machine :D")
    else:
        #clear()
        print('Not a valid input')
