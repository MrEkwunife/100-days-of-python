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
    letter_lst.append(random.choice(pass_makers.letters))
for i in range(0, nr_symbols):
    symbol_lst.append(random.choice(pass_makers.symbols))
for i in range(0, nr_numbers):
    number_lst.append(random.choice(pass_makers.numbers))

passwd = letter_lst + symbol_lst + number_lst
random.shuffle(passwd)

print(''.join(passwd))

