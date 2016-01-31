import os

class View:

	def __init__(self):
		self.setControllerPointer(None)

	def setControllerPointer(self,pointer):
		self.controllerPointer = pointer

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

		result = self.controllerPointer.notifyChosenOp(option)
		return result

	def dutchSearchScreen(self):
		unusedSysReturn = os.system('clear')
		dutchWord = input("Insert the word to be translated: ")
		self.controllerPointer.notifyDutchSearch(dutchWord)

	def engSearchScreen(self):
		unusedSysReturn = os.system('clear')
		engWord = input("Insert the word to be translated: ")
		self.controllerPointer.notifyEngSearch(engWord)

	def insertWordsScreen(self):
		unusedSysReturn = os.system('clear')
		dutchWord = input("Insert the Word in Dutch: ")
		engWord = input("Insert its english translation: ")
		self.controllerPointer.notifyNewEntry(dutchWord,engWord)

	def removeDutchWordScreen(self):
		unusedSysReturn = os.system('clear')
		dutchWord = input('Insert the Word in Dutch to be removed with all of its translations: ')
		self.controllerPointer.notifyDutchRemoval(dutchWord)

	def printDutchResult(self,resultList):
		unusedSysReturn = os.system('clear')
		print('\t\t\tSearch Result(s):\n')
		for element in resultList:
			print('(Dutch, English):',element)
		trash = input('')

	def printEngResult(self,resultList):
		unusedSysReturn = os.system('clear')
		print('\t\t\tSearch Result(s):\n')
		for element in resultList:
			print('(Dutch, English):',element)
		trash = input('')