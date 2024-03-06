# 100 days of coding - Python
# Day 7: Hangman
# By Felipe Rojas
# Learning how to use multiple files in python by importing them into the main file.
# Using While loops to keep the code running


import random
import hangman_art as art
import hangman_words as words

print(art.logo)
print("Welcome to the Hangman, by Felipe Rojas")
print("You have 6 lives")

end_of_game = False
lives = 6

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable 
#called chosen_word.
chosen_word = random.choice(words.word_list)
#print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase.
display = []
for letters in chosen_word:
  display += "_"
  

print(art.stages[lives])
print("The word to guess is: ", display)


while not end_of_game:
    user_guess = input("Guess a letter: ").lower()
    #print(f"user input is {user_guess}")
    
    #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    for position in range(len(chosen_word)):
        if user_guess == chosen_word[position]:
            #print("Guessed a letter!")
            display[position] = user_guess
            
    if user_guess not in chosen_word:
        
        lives -= 1
        print(f"You lose a life, you have {lives} left")
        if lives == 0:
            print("Game over")
            print(f"the word was: {chosen_word}")
            end_of_game = True
        
    print(display)
    if not "_" in display:
        print("Player wins!")
        end_of_game = True
        
    print(art.stages[lives])
