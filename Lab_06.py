"""
Author: PLMM Jiayu Chen
Date:   2020/07/03
Goal:
	1.familarity with string manipulation
	2.loops and iteration
	3. mutable and immutable
Ref:
	USC ITP-115 HW-02
"""
# word_manipulation=input("type the words you want to manipulate")
# word_manipulation.upper()
# word_manipulation()
def check_anagrams(no_space1,no_space2):
	Flag=True
	if(sorted(no_space1)==sorted(no_space2)):
		return Flag
	else:
		Flag=False
		return Flag


def ispalidromeornot(no_space):
	Flag=True
	for i in range (0,int(len(no_space)/2)):
		if no_space[i]!=no_space[len(no_space)-i-1]:
			Flag=False
			break
	return Flag


word_manipulation1=input("type the first statement you want to manipulate: ")
word_manipulation2=input("please type the second statememt you want to manipulate: ")
# print(word_manipulation.upper())
upper_word1=word_manipulation1.upper()
upper_word2=word_manipulation2.upper()
# strip all spaces
split_upper_word1=upper_word1.split()
split_upper_word2=upper_word2.split()
no_space1=""
no_space2=""
no_space1=no_space1.join(split_upper_word1)
no_space2=no_space2.join(split_upper_word2)




if check_anagrams(no_space1, no_space2):
	print("anagrame")
else:
	print("Not anagrame")




# Flag = True
# for i in range (0,int(len(no_space1)/2)):
# 	if no_space1[i]!=no_space1[len(no_space1)-i-1]:
# 		Flag = False
# 		break
#
# if Flag:
# 	print("Palindrome")
# else:
# 	print("Not Palindrome")
#
# Flag = True
# for i in range (0,int(len(no_space2)/2)):
# 	if no_space2[i]!=no_space2[len(no_space2)-i-1]:
# 		Flag = False
# 		break
#
if ispalidromeornot(no_space1) is True:
	print("Palindrome")
else:
	print("Not Palindrome")

if ispalidromeornot(no_space2) is True:
	print("Palindrome")
else:
	print("Not Palindrome")