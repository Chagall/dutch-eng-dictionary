import os
import sqlite3

# Function Name : Create Dictionary Table
# Parameters: 
#	1 - cursor : A cursor to the database connection to provide the means to alter it
# Return: None
# What it does: Creates the Dictionary Table if it does not exist
def createDicTable(cursor):
	cursor.execute('CREATE TABLE IF NOT EXISTS Dictionary(dutchWord TEXT, engWord TEXT)')	

# Function Name : Home Screen
# Parameters: 
#	1 - loop: A boolean value that maintains the screen while it is True
#	2 - connection : a connection to the dictionary database
#	3 - cursor : A cursor to the database connection to provide the means to alter it
# Return: the loop variable
# What it does: Presents the text based user interface
def homeScreen(loop,connection,cursor):

	unusedSysReturn = os.system('clear')
	print('\t\t   Dutch-English Personal Dictionary\n')
	print('\t\tBased on my studies of Dutch on Duolingo\n')
	print('\t\t\tBy: Chagall Khan\n')
	print('\t\t\t     Options:\n')
	print('\t\t1 - Search for a word in Dutch.')
	print('\t\t2 - Search for a word in English.')
	print('\t\t3 - Insert new vocabulary.')
	print('\t\t4 - Remove a word in Dutch and all of its translations.')
	print('\t\t0 - Quit Program.\n')

	chosenOption = input("\t\tChoose an option: ")
	chosenOption = int(chosenOption)

	if(chosenOption == 1):
		# Searches for a word in dutch and return its translations
		dutchSearch(cursor)
		# keeps the main screen loop afterwards			
		return loop		
	elif(chosenOption == 2):
		# Searches for a word in english and return its translations
		engSearch(cursor)
		# keeps the main screen loop afterwards
		return loop		
	elif(chosenOption == 3):
		# Permits the insertion of a word and its translation
		insertWords(connection,cursor)
		# keeps the main screen loop afterwards
		return loop
	elif(chosenOption == 4):
		# Remove a Dutch Word and its translations
		removeLineDutch(connection,cursor)
		# keeps the main screen looop afterwards
		return loop
	elif(chosenOption == 0):
		# Exits the program
		loop = True
		return loop
	
def dutchSearch(cursor):
	unusedSysReturn = os.system('clear')
	dutchWord = input("Insert the word to be translated: ")
	dutchWord = (dutchWord,)
	for row in cursor.execute('SELECT * FROM Dictionary WHERE dutchWord=? COLLATE NOCASE', dutchWord):
		print('(Dutch, English):',row)	
	trash = input('')

def engSearch(cursor):
	unusedSysReturn = os.system('clear')
	engWord = input("Insert the word to be translated: ")
	engWord = (engWord,)
	for row in cursor.execute('SELECT * FROM Dictionary WHERE engWord=? COLLATE NOCASE', engWord):
		print('(Dutch, English):',row)
	trash = input('')

def insertWords(connection,cursor):
	unusedSysReturn = os.system('clear')
	dutchWord = input("Insert the Word in Dutch: ")
	engWord = input("Insert its english translation: ")
	cursor.execute('INSERT INTO Dictionary (dutchWord,engWord) VALUES(?,?)', (dutchWord,engWord))
	connection.commit()
	print('Success!')
	trash = input('')

def removeLineDutch(connection,cursor):
	unusedSysReturn = os.system('clear')
	dutchWord = input('Insert the Word in Dutch to be removed with all of its translations: ')
	cursor.execute('DELETE FROM Dictionary WHERE dutchWord=?', (dutchWord,))
	connection.commit()
	print('Success!')
	trash = input('')
