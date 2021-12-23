import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

print("Welcome to the Rock Paper Scissors game, by Felipe Rojas")
player_selection = input("make your choice (rock, paper or scissors: ").lower()

computer_selection = random.randint(1, 3)
#print(player_selection)
#print(computer_selection)

if player_selection == 'rock':
  if computer_selection == 1:
    print("\nPlayer chooses rock:")
    print(rock)
    
    print(rock)
    print("Computer chooses rock:")

    print("\n Its a tie!")

  if computer_selection == 2:
    print("\nPlayer chooses rock:")
    print(rock)
    
    print(paper)
    print("Computer chooses paper:")

    print("\n Computer wins!")

  if computer_selection == 3:
    print("\nPlayer chooses rock:")
    print(rock)
    
    print(scissors)
    print("Computer chooses scissors:")

    print("\n Player wins!")

elif player_selection == 'paper':
  if computer_selection == 1:
    print("\nPlayer chooses paper:")
    print(paper)
    
    print(rock)
    print("Computer chooses rock:")

    print("\n Player wins!")

  if computer_selection == 2:
    print("\nPlayer chooses paper:")
    print(paper)
    
    print(paper)
    print("Computer chooses paper:")

    print("\n Its a tie!")

  if computer_selection == 3:
    print("\nPlayer chooses paper:")
    print(paper)
    
    print(scissors)
    print("Computer chooses scissors:")

    print("\n Computer wins!")

elif player_selection == 'scissors':
  if computer_selection == 1:
    print("\nPlayer chooses scissors:")
    print(scissors)
    
    print(rock)
    print("Computer chooses rock:")

    print("\n Computer wins!")

  if computer_selection == 2:
    print("\nPlayer chooses scissors:")
    print(scissors)
    
    print(paper)
    print("Computer chooses paper:")

    print("\n Player wins!")

  if computer_selection == 3:
    print("\nPlayer chooses scissors:")
    print(scissors)
    
    print(scissors)
    print("Computer chooses scissors:")

    print("\n Its a tie!")

else:
  print("Not a valid option :( ")