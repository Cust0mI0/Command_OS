__author__ = 'Danny de Snoo'

# Import de OS ,Time en Sys
import os
import time
import sys
import platform
# Import alle Sub systems
from sub_system import *
from sub_Textpad import *
from sub_Date import *
from sub_Weather import *
from sub_Calc import *
from sub_Custom import *

search = ""

#Hierin defineren we wat de List() doet
def List():
	search = input("what would you like to do (Type List for a list of commands) : ")
	if search in ["List", "list"] :
		CommandList()
	#Textpad Command
	elif search in ["Textpad", "textpad"] :
		Textpad()
	#Date command
	elif search in ["Date", "date"] :
		Date()
	#Weathor command
	elif search in ["Weahter", "weather"] :
		Weahter()
	#Calculator command
	elif search in ["Calculator", "calculator"] :
		Calculator()
	#Custom command
	elif search in ["Custom", "custom"] :
		Custom()
	elif search in ["Credits", "credits"] :
		Credits()
	elif search in ["SysInfo", "Sysinfo", "sysInfo", "sysinfo"] :
		Credits()
	elif search in ["May the force be with you", "A New Hope"] :
		A_NEW_HOPE()
	elif search in ["Once more the sith will rule the Galaxy"] :
		Once_More_The_Sith_Will_Rule_The_Galaxy()
	#Quit command
	elif search in ["Shutdown", "shutdown", "Quit", "quit", "Q", "q"] :
		Quit()
	else :
		print("Invalid command, please enter a Valid command")

#Hier Defineren wij de CommandList() waarin staat wat de tot nu toe gemaakte commands doen
def CommandList():
	print(" ")
	print("Here is a list of commands:")
	print(" ")
	print("Textpad    - Texteditor")
	print("Date       - Gives the current date")
	print("Weahter    - Gives current weather data (INTERNET CONNECTION REQUIRED)")
	print("Calculator - Calculator (Simple text based calculator)")
	print("Custom     - Run your own Python files")
	print("SysInfo    - Gives all the system information and OS information")
	print("Shutdown   - Exit Command_OS")
	print(" ")
	print("This is the complete command list for Command_ OS release Alpha 1.1")
	print("Data from the Weahter function is aquired from OpenWeahterMap.org")
	print(" ")

# Hierin geven wij aan dat Het progamma Textpad moet openen
def Textpad():
	Open_Textpad()

def Date():
	Give_Date()

def Weahter():
	print(" ")
	print("Data from the Weahter function is aquired from OpenWeahterMap.org")
	time.sleep(1)
	Open_Weather()

def Calculator():
	Open_Calculator()

def Custom():
	Open_Custom()

def Quit():
	sys.exit()

while search != "#%#$#$#$":
	List()
