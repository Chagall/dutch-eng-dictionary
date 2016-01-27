# --- Imports ---
import os
import sqlite3	
from dicFunctions import * 

# --- Connecting to the Dictionary Databas
conn = sqlite3.connect('DutchEngDic.db')	# Opens and returns a connection the the Dictionary Database
dbCursor = conn.cursor()					# Creates and returns a cursor to manipulate de Database
createDicTable(dbCursor)					# Creates the Eng-Dutch Words Table in the Database if it des not exist

# Keeps the Home Screen loop until the user wishes to leave the program
mayIQuit = False

while(mayIQuit == False):
	mayIQuit = homeScreen(mayIQuit,conn,dbCursor)

# -- Closes the Database Connection before exiting the program
conn.close()