from View import *
from Controller import *
from Model import *

# Instantiating the MVC classes of the Dictionary
textInterface = View()
cont = Controller()
mod = Model()

# Establishing the MVC connection between the objects
textInterface.setControllerPointer(cont)
cont.setModelPointer(mod)
mod.setViewPointer(textInterface)

# Keeps the Home Screen loop until the user wishes to leave the program
mayIQuit = False

while(mayIQuit == False):
	mayIQuit = textInterface.homeScreen()