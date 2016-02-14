import os

class View:

	def __init__(self):
		# This class has a pointer to a controller object to pass messages to it
		# At the instantiation moment the pointer is set to be null
		self.setControllerPointer(None)

	def setControllerPointer(self,pointer):
		self.controllerPointer = pointer

	# Prints the program main screen
	def homeScreen(self):

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

		option = input("\t\tChoose an option: ")
		option = int(option)

		# View notifies Model, throught the Controller, of the chosen option
		result = self.controllerPointer.notifyChosenOp(option)
		return result

	# Prints the dutch word search screen and receives the user input
	def dutchSearchScreen(self):
		unusedSysReturn = os.system('clear')
		dutchWord = input("Insert the word to be translated: ")
		self.controllerPointer.notifyDutchSearch(dutchWord)

	# Prints the english word search screen and receives the user input
	def engSearchScreen(self):
		unusedSysReturn = os.system('clear')
		engWord = input("Insert the word to be translated: ")
		self.controllerPointer.notifyEngSearch(engWord)

	# Prints the word inserting screen and receives the user input
	def insertWordsScreen(self):
		unusedSysReturn = os.system('clear')
		dutchWord = input("Insert the Word in Dutch: ")
		engWord = input("Insert its english translation: ")
		self.controllerPointer.notifyNewEntry(dutchWord,engWord)

	# Prints the word removal screen
	def removeDutchWordScreen(self):
		unusedSysReturn = os.system('clear')
		dutchWord = input('Insert the Word in Dutch to be removed with all of its translations: ')
		self.controllerPointer.notifyDutchRemoval(dutchWord)

	# Prints the result of the dutch word search
	def printDutchResult(self,resultList):
		unusedSysReturn = os.system('clear')
		print('\t\t\tSearch Result(s):\n')
		for element in resultList:
			print('(Dutch, English):',element)
		trash = input('')

	# Prints the result of the english word search
	def printEngResult(self,resultList):
		unusedSysReturn = os.system('clear')
		print('\t\t\tSearch Result(s):\n')
		for element in resultList:
			print('(Dutch, English):',element)
		trash = input('')