__author__ = 'Danny de Snoo'

from Main import *

def Open_Calculator():
	print("Which calculation would you like to preform?")
	print(" ")
	print("--------------------------------------------")
	print("Add, + or 1        -  Addition")
	print("Sub, - or 2        -  Subtraction")
	print("Multi, * or 3      -  Multiplication")
	print("Div, /, : or 4     -  Division")
	print("Quit, Q or 5       -  to exit")
	print("--------------------------------------------")

	choice = input("Enter your choice: ")

	if choice in ["Quit", "quit", "Q", "q", "5"]:
		List()

		num1 = float(input("Enter the 1st number: "))
		num2 = float(input("Enter the 2de number: "))

		if choice in ["Add", "add", "+", "1"] :
			add(num1,num2)
		elif choice in ["Sub", "sub", "-", "2"]:
			Subtract(num1,num2)
		elif choice in ["Multi", "multi", "*", "3"]:
			Multiplication(num1,num2)
		elif choice in ["Div", "div", "/", ":", "4"]:
			Division(num1,num2)
		else:
			print("Invalid choice, please enter a valid number")