import random

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
def random_card_selection():
    random_num = random.randint(0, len(cards)-1)
    selected_card = cards[random_num]
    #print(selected_card)
    if selected_card == 'A':
        return 11
    elif selected_card == 'J' or selected_card == 'Q' or selected_card == 'K':
        return 10
    else:
        return selected_card
        