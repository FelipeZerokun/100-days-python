from art import logo, vs
import random
from game_data import data

print("Welcome to the Higher-Lower game, by Felipe Rojas")
print("You have to guess WHO has more followers on Instagram")

WIN_STREAK = 0
game_over = False

# My first step is to try and get different options

A_option = random.choice(data)
B_option = random.choice(data)
#print(first_option)

# now I'll play with the dictionaries
#print(A_option["name"])
#print(A_option["description"])

#print(f'A is: {A_option["name"]} a {A_option["description"]} from {A_option["country"]} with {A_option["follower_count"]}')
#print(f'B is: {B_option["name"]} a {B_option["description"]} from {B_option["country"]} with {B_option["follower_count"]}')

# My second step is to create a Function which will compare the options

def compare_options(user_choice, A, B):
    #print(A["name"])
    #print(B["name"])
        
    if A["follower_count"] > B["follower_count"]:
        higher_option = 'A'

    elif B["follower_count"] > A["follower_count"]:
        higher_option = 'B'
    else:
        print("Something went wrong :(")
        
    if user_choice == higher_option:
        print("You got it right!")
        return B, True
    else:
        print("Wrong :(")
        return B, False
    
    #print(higher_option)
    return 

    
# My next step is to create the Game function where the user will stay until they lose

def game_loop():
    right_answer = True
    
    global WIN_STREAK
    while right_answer:
        correct_input = False
    
        B_option = random.choice(data)
        if WIN_STREAK == 0:
            A_option = random.choice(data)
            B_option = A_option # Testing duplicated
        
        while A_option["name"] == B_option["name"]:
            print("Got a duplicated!")
            print(f'{A_option["name"]} and {A_option["name"]}')
            B_option = random.choice(data)
            
            
        print(logo)
        print(f"Your winstreak is {WIN_STREAK}")
        print(f'Compare A: {A_option["name"]} a {A_option["description"]} from {A_option["country"]}')
        print(vs)
        print(f'Against B: {B_option["name"]} a {B_option["description"]} from {B_option["country"]}')
        
        while not correct_input:
            user_choice = input("Who has more followers? (A or B): ").upper()
            
            if user_choice == 'A' or user_choice == 'B':
                correct_input = True
            else:
                print("Invalid Input")
        
        A_option, right_answer = compare_options(user_choice, A_option, B_option)
        if right_answer == True:
            WIN_STREAK += 1
        else:
            print(f"Your final score is {WIN_STREAK}")
        
game_loop()