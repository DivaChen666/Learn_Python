"""
Author: PLMM Jiayu Chen
Date:   2020/07/05
Goal:
	1. while loop/print statement

Ref:
	USC ITP-115 HW-03
"""
def triangle(num_line):
	large_num_symbols = 1+2*(num_line-1)
	for n in range(1,num_line+1):
		num_symbols=1+2*(n-1)
		num_space=large_num_symbols-num_symbols
		print(" "*num_space,end="")
		print(" ^"*num_symbols)
		# print(num_symbols,num_space)

input_line_num=input("How many lines do you need(Positive Number)?").strip()

while not input_line_num.isnumeric():
	input_line_num=input("How many lines do you need(Positive Number)?").strip()

input_line_num= int(input_line_num)
triangle(input_line_num)