#!/usr/bin/python3
import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
rand_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
usr_guess = input("Enter your guess letter: ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for let in rand_word:
    if usr_guess == let:
        print("Right")
    else:
        print("Wrong")
