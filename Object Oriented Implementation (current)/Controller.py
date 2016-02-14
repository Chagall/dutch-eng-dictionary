class Controller:

	def __init__(self):
		# This class has a pointer to a model object to pass messages to it
		# At the instantiation moment the pointer is set to be null
		self.setModelPointer(None)

	def setModelPointer(self,pointer):
		self.modelPointer = pointer

	# Notifies model of the user's option so that it can decide
	# wether to close the program or switch to the user's choice
	# screen
	def notifyChosenOp(self,option):
		result = self.modelPointer.setHomeScreenOp(option)
		return result
	
	# Notifies the Model that the user has searched for a
	# translation of a Dutch word
	def notifyDutchSearch(self,word):
		self.modelPointer.retrieveDutchTrans(word)
	
	# Notifies the Model that the user has searched for a
	# translation of an English word
	def notifyEngSearch(self,word):
		self.modelPointer.retrieveEngTrans(word)

	# Notifies the Model that the user wishes to insert
	# a dutch word and its translation
	def notifyNewEntry(self,dutchWord,engWord):
		self.modelPointer.newEntry(dutchWord,engWord)

	# Notifies the Model that the user whishes to remove
	# a Dutch word and all of its translations
	def notifyDutchRemoval(self,word):
		self.modelPointer.dutchRemoval(word)