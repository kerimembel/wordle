from datetime import datetime
from random import choice
from time import time
from mysql_db import WordleDB

'''
    This class is used to create the game
'''
class Wordle():

    def __init__(self,chance_count=6):
        self.db = WordleDB()
        self.chance_count = chance_count
        self.selected_word = self.db.select_todays_word()
        self.words =  self.db.select_words()
        self.choose_word()
    
    #This method is used to choose a word from the available words
    def choose_word(self):
        if(self.selected_word == None):
            words = self.db.select_available_words()
            chosen_word = str(choice(words)[0])
            self.db.insert_todays_word(chosen_word)
            self.db.update_available_words(chosen_word)
        else:
            chosen_word = str(self.selected_word[0])

        print(str(datetime.now()) + ": " + "Chosen word: " + chosen_word)
        self.chosen_word = chosen_word.lower()

    def validate_word(self, word):
        word = word.lower()
        if word in self.words:
            return True
        return False
    
    def add_highscore(self, username, highscore):
        return self.db.insert_highscore(username, highscore)

    def get_highscores(self):
        return self.db.select_highscore()

    def get_username(self, client_id):
        username = self.db.select_username(client_id)
        if username:
            return username[0]
        return ""

    def register_user(self, client_id, username):
        return self.db.register_user(client_id, username)

    def update_username(self, client_id, username):
        return self.db.update_username(client_id, username)
