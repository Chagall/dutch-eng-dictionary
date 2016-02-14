import sqlite3	

class Model():

	# Constructor
	def __init__(self):
		self.setHomeScreenOp(-1)
		self.setViewPointer(None)

	# Setters
	def setViewPointer(self,pointer):
		self.viewPointer = pointer

	def setHomeScreenOp(self,option):
		self.homeScreenOp = option
		if(self.getHomeScreenOp() != -1):
			if(self.getHomeScreenOp() == 1):
				self.viewPointer.dutchSearchScreen()
				return False	
			elif(self.getHomeScreenOp() == 2):
				self.viewPointer.engSearchScreen()
				return False
			elif(self.getHomeScreenOp() == 3):
				self.viewPointer.insertWordsScreen()
				return False
			elif(self.getHomeScreenOp() == 4):
				self.viewPointer.removeDutchWordScreen()
				return False
			elif(self.getHomeScreenOp() == 0):
				return True
	
	def getHomeScreenOp(self):
		return self.homeScreenOp

	# Retrieves all tuples  in the database which contains the searched dutch word 		
	def retrieveDutchTrans(self,word):
		dutchWord = (word,)
		resultList = []
		conn = sqlite3.connect('DutchEngDic.db')	# Opens and returns a connection the the Dictionary Database
		dbCursor = conn.cursor()					# Creates and returns a cursor to manipulate the Database
		for row in dbCursor.execute('SELECT * FROM Dictionary WHERE dutchWord=? COLLATE NOCASE', dutchWord):
			resultList.append(row)
		conn.close()
		self.viewPointer.printDutchResult(resultList)

	# Retrieves all tuples  in the database which contains the searched english word 
	def retrieveEngTrans(self,word):
		engWord = (word,)
		resultList = []
		conn = sqlite3.connect('DutchEngDic.db')	# Opens and returns a connection the the Dictionary Database
		dbCursor = conn.cursor()					# Creates and returns a cursor to manipulate the Database
		for row in dbCursor.execute('SELECT * FROM Dictionary WHERE engWord=? COLLATE NOCASE', engWord):
			resultList.append(row)
		conn.close()
		self.viewPointer.printEngResult(resultList)

	# Connects to the dictionary database and inserts a dutchWord with its engWord translation
	def newEntry(self,dutchWord,engWord):
		conn = sqlite3.connect('DutchEngDic.db')	# Opens and returns a connection the the Dictionary Database
		dbCursor = conn.cursor()					# Creates and returns a cursor to manipulate the Database
		try:
			dbCursor.execute('INSERT INTO Dictionary (dutchWord,engWord) VALUES(?,?)', (dutchWord,engWord))
			conn.commit()
			print('Success!')
		except Exception as e:
			print('\nAn error ocurred while inserting the words on the Dictionary.\n')
			print('\t\t\tThe error was:\n')
			print(e)
		conn.close()
		trash = input('')

	# Connects to the dictionary database and removes all tuples which contains dutchWord
	def dutchRemoval(self,dutchWord):
		conn = sqlite3.connect('DutchEngDic.db')	# Opens and returns a connection the the Dictionary Database
		dbCursor = conn.cursor()					# Creates and returns a cursor to manipulate the Database
		try:
			dbCursor.execute('DELETE FROM Dictionary WHERE dutchWord=?', (dutchWord,))
			conn.commit()
			print('Success!')
		except Exception as e:
			print('\nAn error ocurred while deleting the words on the Dictionary.\n')
			print('\t\t\tThe error was:\n')
			print(e)
		conn.close
		trash = input('')
