"""
Author: PLMM Jiayu Chen
Date:   2020/07/03
Goal:
	1. IF/ELSE statement
	2. Print Format
	3. I/O Test
Ref:
	USC ITP-115 HW-02
"""
import random

def Barista():
	coffee_size = input("What size of coffee do you want(S,M,L)?:")
	size_list = ["S", "M", "L"]
	coffee_size = coffee_size.upper().strip()
	while coffee_size not in size_list:
		coffee_size = input("What size of coffee do you want(S,M,L)?:").upper().strip()

	coffee_random_temperature = input("would you like your drink to be a random temperature? ")
	temrandom_list = ["Y", "N"]
	coffee_random_temperature = coffee_random_temperature.upper()
	while coffee_random_temperature not in temrandom_list:
		coffee_random_temperature = input("Would you like your drink to be a random temperature(Y/N)? ").upper()

	if coffee_random_temperature == "Y":
		coffee_temperature = random.randrange(20, 80)
	elif coffee_random_temperature == "N":
		coffee_temperature = int(input("What temperature do you like(in degree)?:"))
		while coffee_temperature not in range(100):
			coffee_temperature = int(input("What temperature do you like(in degree)?:"))

	coffee_type = input("What type of beans/blend would you like?:")  # Assume Correct Input

	coffee_room = input("Would you like room for the cream(Y/N)?:")
	room_list = ["Y", "N"]
	coffee_room = coffee_room.upper()
	while coffee_room not in room_list:
		coffee_room = input("Would you like room for the cream(Y/N)?:").upper()

	Final_Sen = "You ordered a "
	if coffee_size == "S":
		Final_Sen = Final_Sen + "small "
	elif coffee_size == "M":
		Final_Sen = Final_Sen + "medium "
	elif coffee_size == "L":
		Final_Sen = Final_Sen + "large "

	if coffee_temperature in range(50):
		Final_Sen = Final_Sen + "iced "
	elif coffee_temperature in range(50, 100):
		Final_Sen = Final_Sen + "hot "

	Final_Sen = Final_Sen + coffee_type + " "

	if coffee_room == "Y":
		Final_Sen = Final_Sen + "with cream."
	elif coffee_room == "N":
		Final_Sen = Final_Sen + "with no cream."
	return Final_Sen

random_sentence=Barista()
print(random_sentence)