"""
Author: PLMM Jiayu Chen
Date:   2020/07/08
Goal:
	1. familiarity with loops(while/for)
	2.familarity with if/else statement

Ref:
	USC ITP-115 HW-03
"""
def temperatureConverter():
	WelcomeWord="welcome to the temperature Converter 1.0"
	print(WelcomeWord)

	selection_list=["1","2"]
	user_selection=input("Enter 1 for F->C, or 2 for C->F:")
	while user_selection not in selection_list:
		user_selection=input("Please enter 1 for F->C, or 2 for C->F:")

	if user_selection=="1":
		temperature_insertion=input("Enter input temperature: ")
		if temperature_insertion.isnumeric()!=True:
			print("Invalid Conversion Code")
			return 0
		converted_temperature=(int(temperature_insertion)-32)*5/9
		# print("The converted_temperature is",converted_temperature)
	elif user_selection=="2":
		temperature_insertion = input("Enter input temperature: ")
		if temperature_insertion.isnumeric()!=True:
			print("Invalid Conversion Code")
			return 0
		converted_temperature = int(temperature_insertion)*9/5+32
		# print("The converted_temperature is",converted_temperature)

	return converted_temperature

def wantsToContinue():
	wantsToContinue=input("Do you want to continue? ").upper()
	continueselection_list=["Y","N"]
	while wantsToContinue not in continueselection_list:
		wantsToContinue=input("Do you want to continue? ").upper()

	if wantsToContinue=="Y":
		return True
	elif wantsToContinue=="N":
		return False


def main():
	Temp_converted = temperatureConverter()
	print("The converted temperature is", Temp_converted)
	continueOrNot = wantsToContinue()
	while continueOrNot is True:
		Temp_converted = temperatureConverter()
		print("The converted temperature is", Temp_converted)
		continueOrNot = wantsToContinue()

main()