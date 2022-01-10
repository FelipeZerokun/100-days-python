from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO 1. First, I will create the objects necessary for the coffee machine
my_menu = Menu()
# print(my_menu.get_items())
my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
on_state = True

# TODO 2. Now, I will create the loop where my coffee machine is going to stay.

while on_state:

    user_choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    user_order = my_menu.find_drink(user_choice)
    # print(user_order.name)

    # TODO 3. I will create the three possible instances for the machine

    # First, If the user turns off the machine
    if user_choice == "off":
        print("Thanks for user the Coffee Machine :D ")
        on_state = False

    # Second, If the user asks for a report
    elif user_choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()

    # Third, if the user asks for coffee
    elif user_order != None:
        print(f"You chose {user_order.name}!")

        # TODO 4. Firstly, check if there are enough ingredients.
        can_make = my_coffee_machine.is_resource_sufficient(user_order)
        if can_make:
            # TODO 4. Now, let's ask for the money
            is_enough = my_money_machine.make_payment(user_order.cost)
            if is_enough:
                my_coffee_machine.make_coffee(user_order)

    # Finally, if the user enters an invalid input
    else:
        print("Not a Valid input")