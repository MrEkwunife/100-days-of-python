import pass_makers
import random

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_lst = []
symbol_lst = []
number_lst = []

for i in range(0, nr_letters):
    letter_lst.append(pass_makers.letters[random.randint(0, nr_letters - 1)])
for i in range(0, nr_symbols):
    symbol_lst.append(pass_makers.symbols[random.randint(0, nr_symbols - 1)])
for i in range(0, nr_numbers):
    number_lst.append(pass_makers.numbers[random.randint(0, nr_numbers - 1)])

passwd = letter_lst + symbol_lst + number_lst
random.shuffle(passwd)

print(''.join(passwd))

