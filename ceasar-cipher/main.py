#!/usr/bin/python3
from art import logo
import os

play_again = True
while play_again:
	print(logo)

	#Ask user to input encode or decode
	encode_decode = input("Enter 'encode' or 'decode': ").lower()
	while encode_decode not in ['encode', 'decode']:
		encode_decode = input("You have to enter 'encode' to encode a text or 'decode' to decode a text: ")

	#Ask user to input texts
	characters = input(f"Input characters to be {encode_decode}d: ")
	#Ask user to input shits

	while True:
		try:
			shifts = int(input("Enter a shift amount: "))
			break
		except ValueError:
			print("Shift should be an int")
			
	def ceasar(ed_char, shift_sp, ed_choice):
		conv_txt = ""

		if ed_choice == "decode":
			shift_sp *= -1
			
		for i in range(0, len(ed_char)):
			if ed_char[i].islower():
				conv_txt += chr((ord(ed_char[i]) - ord('a') + shift_sp) % 26 + ord('a'))
			elif ed_char[i].isupper():
				conv_txt += chr((ord(ed_char[i]) - ord('A') + shift_sp) % 26 + ord('A'))
			else:
				conv_txt += ed_char[i]

		print(f"Your {encode_decode}d text is: {conv_txt}")

	ceasar(characters,shifts,encode_decode)

	cont = input("\nEnter yes continue or no to exit: ")
	while cont not in ['yes', 'no', 'y', 'n']:
		cont = input("Enter yes or no!: ")
	if cont == 'n' or cont == 'no':
		play_again = False

	os.system('clear')