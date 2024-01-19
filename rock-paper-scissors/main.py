#!/usr/bin/python3
import hands, random

ava_hands = [hands.rock, hands.paper, hands.scissors]

n = 1
while (n):
    human_hand_inp = input("Enter 'rock', 'paper', 'scissors': ").lower()
    if human_hand_inp in ['rock', 'paper', 'scissors']:
        n = 0
if human_hand_inp == 'rock':
    hand_indx = 0
elif human_hand_inp == 'paper':
    hand_indx = 1
else:
    hand_indx = 2

comp_hand = ava_hands[random.randint(0,2)]
human_hand = ava_hands[hand_indx]

print(f"Computer: {comp_hand} vs\n Human: {human_hand}")

if comp_hand == ava_hands[0] and human_hand == ava_hands[1]:
    print("You Win!")
elif comp_hand == ava_hands[1] and human_hand == ava_hands[2]:
    print("You Win!")
elif comp_hand == ava_hands[2] and human_hand == ava_hands[0]:
    print("You Win!")
elif human_hand == ava_hands[0] and comp_hand == ava_hands[1]:
    print("You Loose!")
elif human_hand == ava_hands[1] and comp_hand == ava_hands[2]:
    print("You Loose!")
elif human_hand == ava_hands[2] and comp_hand == ava_hands[0]:
    print("You Loose!")
else:
    print("Draw!")
