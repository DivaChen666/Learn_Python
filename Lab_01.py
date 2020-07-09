"""
Author: Jiayu Chen
Date:   2020/07/03
Goal:
	1. Print Test
	2. Print Format
	3. I/O Test
Ref:
	USC ITP-115 HW-01
"""
def print_box():
	print(" --- ")
	print("|   |")
	print("|   |")
	print("|___|")


def print_sentence():
	print("you don't frighten us, English is pig-dog\n"
      + "go and boil your bottoms,son of a silly person\n"
      + "              " + "-\"Monty python and the Holly Gail\"")


def print_date():
	month = input("what month are we in?:")
	day=input("what day is it?：")
	the_day_of_the_month=int(input("what day of the month is today?:"))
	print("Today is "+ day,month,the_day_of_the_month,"and Tommorrow will be", month, the_day_of_the_month+1)


def main():
	print_box()
	print_sentence()
	print_date()

main()