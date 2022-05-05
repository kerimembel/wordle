import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

'''
    This class is used to connect to the database and perform queries
'''
class WordleDB():

  def __init__(self):
    self.conn = pymysql.connect(
      host =      os.getenv("WORDLE_DB_HOST"),
      user =      os.getenv("WORDLE_DB_USER"),
      password =  os.getenv("WORDLE_DB_PASSWORD"),
      database =  os.getenv("WORDLE_DB_NAME")
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
  def insert_highscore(self, name, score):
    cur = self.conn.cursor()
    cur.execute("INSERT INTO high_score (name, score, date) VALUES (%s, %s, CURDATE())", (name, score))
    self.conn.commit()

  #This method is used to insert word into the database
  def insert_word(self, word):
    cur = self.conn.cursor()
    try:
      cur.execute("INSERT INTO words (word) VALUES (%s)", (word,))
    except pymysql.err.IntegrityError:
      print("Word already exists")
      pass
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

  def close(self):
    self.conn.close()

