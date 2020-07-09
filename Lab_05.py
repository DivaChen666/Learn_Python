"""
Author: PLMM Jiayu Chen
Date:   2020/07/05
Goal:
	1. use of the random library
	2.familarity with th elists and list manipulation

Ref:
	USC ITP-115 HW-03
"""

import random


# Option 1: View all words
def view_all_words(articles, nouns, verbs):
	print("articles:", articles)
	print("nouns:", nouns)
	print("verbs:", verbs)


# Option 2: Add new words
def add_new_words(nouns, verbs):
	user_insertion_list=["1","2"]
	user_insertion=input("enter 1 for nouns, enter 2 for verbs: ")
	while user_insertion not in user_insertion_list:
		user_insertion=input("please select 1 or 2: ")

	if user_insertion == "1":
		word_to_add = input("Enter the words: ")
		nouns.append(word_to_add)
		print(nouns)
	elif user_insertion == "2":
		word_to_add = input("Enter the words: ")
		verbs.append(word_to_add)
		print(verbs)


# Option 3: Delete words
def delete_word(nouns, verbs):
	user_delete_list=["1","2"]
	user_delete=input("enter 1 if you want to delete nouns, enter 2 if you want to delete verbs: ")
	while user_delete not in user_delete_list:
		user_delete = input('please select from 1 or 2: ')
	if user_delete=="1":
		nouns_to_delete=input("please select the words you want to delete: ")
		while nouns_to_delete not in nouns:
			nouns_to_delete=input("the words you delete not exits,please type the words in the list: ")
		nouns.remove(nouns_to_delete)
		print("The final version is :",nouns)
	elif user_delete=="2":
		verbs_to_delete=input("please select the words you want to delete: ")
		while verbs_to_delete not in verbs:
			verbs_to_delete=input("the words you delete not exits, please type the words in the list: ")
		verbs.remove(verbs_to_delete)
		print("The final version is: ",verbs)


# Option 4: generator sentence
def generate_sentence(articles, verbs, nouns):
	print(random.choice(articles).capitalize(),random.choice(nouns),random.choice(verbs),random.choice(articles),random.choice(nouns),".")


# Initial words lists
articles_list = ["a", "the"]
nouns_list = ["person", "place", "thing"]
verbs_list = ["danced", "ate", "froliced"]

# Welcome word for the generator
while 1:
	welcome_words = "Welcome to the Sentence Generator\n" \
	                "Menu\n" \
	                "1) View Words\n" \
	                "2) Add Words\n" \
	                "3) Remove Words\n" \
	                "4) Generator Sentence\n" \
	                "5) Exit"
	print(welcome_words)



	welcome_words_list=["1","2","3","4","5"]
	generating_sentence=input("please select the options from welcome_words:  ")
	while generating_sentence not in welcome_words_list:
		generating_sentence=input("Wrong input, please select the options from welcome_words:  ")

	if generating_sentence=="1":
		view_all_words(articles_list, nouns_list, verbs_list)
	elif generating_sentence == "2":
		add_new_words(nouns_list, verbs_list)
	elif generating_sentence == "3":
		delete_word(nouns_list, verbs_list)
	elif generating_sentence == "4":
		generate_sentence(articles_list, nouns_list, verbs_list)
	elif generating_sentence == "5":
		break
	print("\n\n")