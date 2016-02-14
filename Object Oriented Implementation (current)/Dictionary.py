from View import *
from Controller import *
from Model import *

# Instantiating the MVC classes of the Dictionary
textInterface = View()	# Class responsible for printing the text interface and receiving inputs
cont = Controller()		# Middleware between View and Model
mod = Model()			# Stores and retrieves database informations

# Establishing the MVC connection between the objects so that they can communicate
textInterface.setControllerPointer(cont)
cont.setModelPointer(mod)
mod.setViewPointer(textInterface)

# Keeps the Home Screen loop until the user wishes to leave the program
mayIQuit = False

while(mayIQuit == False):
	mayIQuit = textInterface.homeScreen()