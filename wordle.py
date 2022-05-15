from random import choice
from mysql_db import WordleDB

'''
    This class is used to create the game
'''
class Wordle():

    def __init__(self,chance_count=6):
        self.db = WordleDB()
        self.chance_count = chance_count
        self.selected_word = self.db.select_todays_word()
        self.chosen_word = self.choose_word()
        self.words =  self.db.select_words()
    
    #This method is used to choose a word from the available words
    def choose_word(self):
        if(self.selected_word == None):
            words = self.db.select_available_words()
            chosen_word = str(choice(words)[0])
            self.db.insert_todays_word(chosen_word)
            self.db.update_available_words(chosen_word)
        else:
            chosen_word = str(self.selected_word[0])

        return chosen_word.lower()

    def validate_word(self, word):
        word = word.lower()
        if word in self.words:
            return True
        return False
    
    def add_highscore(self, username, highscore):
        return self.db.insert_highscore(username, highscore)

    def get_highscores(self):
        return self.db.select_highscore()
