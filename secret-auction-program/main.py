#!/usr/bin/python3

from art import logo
from os import system

more_bidders = True
bidders_nd_amount = {}

while more_bidders:
    system('clear')
    print(logo)

    b_name = input("Enter your name: ")

    while b_name in bidders_nd_amount:
        b_name = input("Bidder with name already exits. Use another name: ")

    while True:
        try:
            bid_amt = int(input("Enter your bid amount $: "))
            while bid_amt < 1:
                bid_amt = int(input("Bid amount cannot be less than 1 $: "))
            break
        except ValueError:
            print("Enter a valid amount")
            
    bidders_nd_amount[b_name] = bid_amt

    is_more_bidders = input("Are there more bidders? (yes or no): ")

    while is_more_bidders not in ['yes', 'no']:
        is_more_bidders = input("Enter 'yes' or 'no': ")

    if is_more_bidders == 'no':
        more_bidders = False


def bid_winner(bidders_nd_amount):
    hi_bid_amt = 0
    hi_bid = None

    for key, value in bidders_nd_amount.items():
        if value > hi_bid_amt:
            hi_bid_amt = value
            hi_bid = key
    
    print(f"The highest bider is {hi_bid} with a bid of {hi_bid_amt}")

bid_winner(bidders_nd_amount)



    
    