# Day 11 of 100: BlackJack Capstone proyect by Felipe Rojas

from card_selection import random_card_selection

print("Welcome to the BlackJack Game, by Felipe Rojas")


def blackjack_game():
    
    player_A = False
    dealer_A = False
    # First, I will set the Player and Dealer's cards
    player_hand = []
    dealer_hand = []
    
    for i in range(2):
         player_hand.append(random_card_selection())
         dealer_hand.append(random_card_selection())
        
    
    print(f"Your hand is {player_hand}")
    print(f"Dealer hand is [{dealer_hand[0]}] [X]")
    
    add_cards = True
    player_lose = False
    dealer_low_hand = True
    while add_cards:
        player_add = input("Do you want to add a card to your hand? (yes or no): ").lower()
        if player_add == "yes":
            player_hand.append(random_card_selection())
            print(f"Your hand is {player_hand}")
            if sum(player_hand) > 21:
                if 11 in player_hand:
                    print("You got an A")
                    
                    a_index = player_hand.index(11)
                    player_hand[a_index] = 1
                    print("You new hand is", player_hand)
                    
                else:
                    print("you got over 21")
                    add_cards = False
                    player_lose = True
            
        elif player_add == "no":
            add_cards = False
            
        else:
            print("Not a valid input")
    
    if player_lose == True:
        print("You lose")
        
    else:
        while dealer_low_hand:
            if sum(dealer_hand) <12:
                dealer_hand.append(random_card_selection())

            else:
                dealer_low_hand = False
                
        print(f"Your hand is {player_hand}")
        print("You add up to",sum(player_hand))
        print(f"Dealer hand is {dealer_hand}")
        print("Dealer hand adds up to", sum(dealer_hand))
    
        if sum(player_hand) > sum(dealer_hand):
            print("You win")
            
        elif sum(player_hand) < sum(dealer_hand):
            print("You lose")
        
        elif sum(player_hand) == sum(dealer_hand):
            print("It's a draw!")
        
    new_game = input("Do you want to start a new game? (yes or no): ").lower()
        
    if new_game == "yes":
        blackjack_game()
    else:
        print("Thank you for playing!")
  
blackjack_game()