"""
Author: PLMM Jiayu Chen
Date:   2020/07/05
Goal:
	1. ASCII
	2.FOR LOOPS
	3.STRING PROCESSING AND INFORMATION MANIPULATION

Ref:
	USC ITP-115 HW-03
"""
# Welcome word print
welcome_word = "Would you like to :\n" \
               "a) See the ASCII code for the alphabet\n" \
               "b) Translate a word into its ASCII code"
print(welcome_word)

# Get the input for the first selection and make sure it is either a or b(Not case sensitive)
initial_slection_list=["a","b"]
initial_selection=input("Select a or b: ").lower()
while initial_selection not in initial_slection_list:
	initial_selection=input("please select the assigned one").lower()

# For the "a" and "b" case
if initial_selection=="a":
	upper_lower_selection=input("do you want to see the alphabet in upper(u) or in lowercase(l)? ").lower()
	selection_list=["u","l"]
	while upper_lower_selection not in selection_list:
		upper_lower_selection=input("you have entered an invalid choice.Please try again.").lower()
	if upper_lower_selection=="l":
		for letter_num in range(ord("a"),ord("z")+1):
			print(letter_num, chr(letter_num))
	if upper_lower_selection=="u":
		for letter_num in range(ord("A"),ord("Z")+1):
			print(letter_num, chr(letter_num))
elif initial_selection=="b":
	word_translation_into_num=input("Please insert the word you would like to translate")
	for letter in word_translation_into_num:
		wangyunjiedashabi="{0}: {1}"
		print(wangyunjiedashabi.format(letter, ord(letter)))