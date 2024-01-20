import hangman_art, hangman_words, os, random

#Getting random word from list of words
get_random_word = random.choice(hangman_words.word_list)
# print(get_random_word)

#List that stores wrong guesses
wrng_guess = []

#List where right guesse would be stored, filled with "_" for len(get_random_word)
rght_guess = []
for i in get_random_word:
    rght_guess += "_"

lives = 6
game_over = False


while not game_over:
    usr_inp = input("Enter a letter: ").lower()

    os.system('cls' if os.name == 'nt' else 'clear')

    for i, j in enumerate(get_random_word):
        if usr_inp == j:
            rght_guess[i] = usr_inp
    
    # Reducing lives if guess is wrong and guess hasn't been inputed b4

    if usr_inp not in get_random_word and usr_inp not in wrng_guess:
        lives -= 1
        wrng_guess.append(usr_inp)

    print("Wrong guess: " + ' '.join(map(str, wrng_guess)))
    print("Right guess: " + ' '.join(map(str, rght_guess)))
    print(hangman_art.stages[lives])
    
    if "_" not in rght_guess:
        print("You win!🥳")
        game_over = True
    
    if lives <= 0:
        print("You Lose!🥲")
        game_over = True


        