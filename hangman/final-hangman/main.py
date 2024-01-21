#!/usr/bin/python3

import hangman_art, hangman_words, os, random, string, time

print(hangman_art.logo)

get_random_word = random.choice(hangman_words.word_list)
# print(get_random_word)

wrng_guess = []

rght_guess = []
for i in get_random_word:
    rght_guess += "_"

lives = 6
game_over = False

start_time = time.time()
while not game_over:
    usr_inp = input("Enter a letter: ").lower()
    while usr_inp not in string.ascii_lowercase:
        usr_inp = input("Enter a valid alphabetical character: ")

    os.system('cls' if os.name == 'nt' else 'clear')

    for i, j in enumerate(get_random_word):
        if usr_inp == j:
            rght_guess[i] = usr_inp
    
    # Reducing lives if guess is wrong and guess hasn't been inputed b4

    if usr_inp not in get_random_word and usr_inp not in wrng_guess:
        lives -= 1
        wrng_guess.append(usr_inp)

    print(hangman_art.logo)
    print("Wrong guess: " + ' '.join(map(str, wrng_guess)))
    print("Right guess: " + ' '.join(map(str, rght_guess)))
    print(hangman_art.stages[lives])
    
    if "_" not in rght_guess:
        print("You win!🥳")
        game_over = True
    
    if lives <= 0 or time.time() - start_time > 50:
        print("You Lose!🥲")
        print(f"The word is {get_random_word}")
        game_over = True


        