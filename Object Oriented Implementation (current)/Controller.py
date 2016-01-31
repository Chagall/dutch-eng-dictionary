class Controller:

	def __init__(self):
		self.setModelPointer(None)

	def setModelPointer(self,pointer):
		self.modelPointer = pointer

	def notifyChosenOp(self,option):
		result = self.modelPointer.setHomeScreenOp(option)
		return result
		
	def notifyDutchSearch(self,word):
		self.modelPointer.retrieveDutchTrans(word)

	def notifyEngSearch(self,word):
		self.modelPointer.retrieveEngTrans(word)

	def notifyNewEntry(self,dutchWord,engWord):
		self.modelPointer.newEntry(dutchWord,engWord)

	def notifyDutchRemoval(self,word):
		self.modelPointer.dutchRemoval(word)