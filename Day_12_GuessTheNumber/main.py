
# 100 days of coding - Python
# Day 12: Guess the number game
# By Felipe Rojas

# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer.
# Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo
import random

print(logo)
print("Welcome to Guess the Number Game, by Felipe Rojas\n\n")

# Function for checking the answers
def guess_game(user_guess):
  if user_guess == number_to_guess:
    print("You got it! Nice work!")
    return 0
  
  elif user_guess > number_to_guess:
    print("Wrong guess. Too High")
    if num_tries == 1:
        print("the number was", number_to_guess)
        print("Game over")
    return num_tries-1

  elif user_guess < number_to_guess:
    print("Wrong guess. Too Low")
    if num_tries == 1:
        print("the number was", number_to_guess)
        print("Game over")
    return num_tries - 1



# I randomly select the number from 1 to 100
number_to_guess = random.randint(1, 100)
#print(f"The number to guess is {number_to_guess}")

print("You have to guess a number between 1 and 100")

good_entry = False
while not good_entry:
  difficulty = input("Choose the difficulty of the game (easy or hard): ").lower()
  if difficulty == "easy":
    num_tries = 10
    good_entry = True
  elif difficulty == "hard":
    num_tries = 5
    good_entry = True
  else:
    print("Not a valid option. Try again")

while num_tries > 0:
  print(f"You have {num_tries} tries left")
  guessed_number = int(input("Enter your guess: "))
  num_tries = guess_game(guessed_number)
