import pymysql
from .environment import get_env

'''
    This class is used to connect to the database and perform queries
'''
class WordleDB():

	def __init__(self):
		self.conn = pymysql.connect(
			host =      get_env("WORDLE_DB_HOST"),
			user =      get_env("WORDLE_DB_USER"),
			password =  get_env("WORDLE_DB_PASSWORD"),
			database =  get_env("WORDLE_DB_NAME")
		)  
	#This method is used to insert todays word into the database
	def insert_todays_word(self, word):
		cur = self.conn.cursor()
		cur.execute("INSERT INTO daily_word (word, date) VALUES (%s, CURDATE())", (word,))
		self.conn.commit()

  	#This method is used to select the todays word from the database
	def select_todays_word(self):
		cur = self.conn.cursor()
		cur.execute("SELECT word FROM daily_word WHERE date = CURDATE()")
		return cur.fetchone()

  	#This method is used to insert the scores of the user into the database
	def insert_highscore(self, username, score):
		cur = self.conn.cursor()
		try:
			cur.execute("INSERT INTO high_score (username, score, date) VALUES (%s, %s, CURDATE())", (username, score))
			self.conn.commit()
			return True
		except pymysql.err.IntegrityError:
			print("This user already has a highscore")
			return False

	#This method is used to select the highscores from the database
	def select_highscore(self):
		cur = self.conn.cursor()
		cur.execute("SELECT username, score FROM high_score WHERE date = CURDATE() ORDER BY score ASC LIMIT 10")
		return list(cur.fetchall())

  #This method is used to insert word into the database
	def insert_word(self, word):
		cur = self.conn.cursor()
		try:
			cur.execute("INSERT INTO words (word) VALUES (%s)", (word,))
		except pymysql.err.IntegrityError:
			print("Word already exists")
			
		self.conn.commit()

	#This method is used to update the status of the word to 1
	def update_available_words(self, word):
		cur = self.conn.cursor()
		cur.execute("UPDATE words SET status = 1 WHERE word = %s", (word,))
		self.conn.commit()

	#This method is used to select the available words from the database
	def select_available_words(self):
		cur = self.conn.cursor()
		cur.execute("SELECT word FROM words WHERE status = 0")
		return list(cur.fetchall())

	#This method is used to select the words from the database
	def select_words(self):
		cur = self.conn.cursor()
		cur.execute("SELECT word FROM words")
		words = list(cur.fetchall())
		word_dictionary = {}
		for word in words:
			word_dictionary[word[0]] = 0
		return word_dictionary

	def close(self):
		self.conn.close()

