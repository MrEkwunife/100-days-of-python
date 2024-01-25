def get_random_cards(card_n):
    ''' 
    get_random_cards - gets number of cards specified in card_n
    @card_n: number of cards to get from the list cards
    return: number of cards specified in card_n

    '''
    import random
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K']

    ch_cards = []

    for i in range(0, card_n):
        ch_cards.append(random.choice(cards))
    return ch_cards

def display_card(pl_card, com_card, n):
    '''
    display_card - prints player's card and computer's card at indx 0 if n < 1
    @pl_card: players card to displayed
    @com_card: computer's card to be displayed
    @n: determines if all computer's should be displayes
    Return: returns nothing but displays card only 
    '''

    print(f"Player Cards: {pl_card}")
    print(f"Computer Card: {com_card[0]}") if n < 1 else print(f"Computer Cards: {com_card}")

def sum_card(cards):
    '''
    sum_card - sums card's value in a card
    @cards: cards whose value are to be added
    Return: sum of card values
    '''

    if isinstance(cards, int):
        return cards

    sum = 0

    for card in cards:
        if card in ['J', 'Q', 'K']:
            sum += 10
        elif card == 'A' and sum <= 10:
            sum += 11
        elif card == 'A' and sum > 10:
            sum += 1
        else:
            sum += card

    return sum

def display_sum(pl_sum, com_sum):
    '''
    display_sum - displays player's sum and computer's sum to the screen
    @pl_sum: player's sum, comp sum
    '''
    print('\n')

    print(f"Player's Sum: {pl_sum}")
    print(f"Computer's Sum: {com_sum}")


def check_winner(pl_sum, com_sum, play_again):
    if com_sum == 21 or pl_sum > 21:
        return "Computer"
    if (pl_sum == 21 or com_sum > 21) and com_sum >= 16:
        return "Player"
    if pl_sum > com_sum and play_again == False:
        return "Player"
    if com_sum > pl_sum and play_again == False:
        return "Computer"


def get_if_more_cards(arg):
    return True if arg == "yes" else False