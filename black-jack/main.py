#!/usr/bin/python3
from helper_funcs import get_random_cards
from helper_funcs import display_card
from helper_funcs import sum_card
from helper_funcs import display_sum
from helper_funcs import check_winner
from helper_funcs import get_if_more_cards

issued_card = {"player_card": [], "computer_card": []}
game_on = True
more_cards = True

issued_card["player_card"].extend(get_random_cards(1))
issued_card["computer_card"].extend(get_random_cards(2))

while game_on:

    if more_cards == True:
        issued_card["player_card"].extend(get_random_cards(1))
        display_card(issued_card["player_card"], issued_card["computer_card"], 0)
        com_sum = sum_card(issued_card["computer_card"][0])
    else:
        issued_card["computer_card"].extend(get_random_cards(1))
        display_card(issued_card["player_card"], issued_card["computer_card"], 1)
        com_sum = sum_card(issued_card["computer_card"])

    pl_sum = sum_card(issued_card["player_card"])

    
    display_sum(pl_sum, com_sum)

    winner = check_winner(pl_sum, com_sum, more_cards)
    if winner == "Computer" or winner == "Player":
        print(f"{winner} wins")
        break
        game_on = False
    else:
        pass
    

    more_cards = get_if_more_cards(input("Do u want more cards?: "))

    # game_on = False
