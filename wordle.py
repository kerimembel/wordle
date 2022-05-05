from random import choice
from module.validator import validate_word
from time import time
from config import  FINISH_GAME, NOT_EXIST, CORRECT_PLACE, WRONG_PLACE, YOU_LOST, YOU_WON, TRY_AGAIN
from model.letter import Letter
from module.mysql_db import WordleDB

'''
    This class is used to create the game
'''
class Wordle():

    def __init__(self,chance_count=6):
        self.db = WordleDB()
        self.chance_count = chance_count
        self.start_time = time()
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
        self.db.insert_highscore(username, highscore)

    def get_highscores(self):
        return self.db.select_highscore()

    def analyze_word(self, word):
        word = word.lower()
        word_analyze = []
        for i in range(len(word)):
            if word[i] in self.chosen_word:
                if(self.chosen_word[i] == word[i]):
                    word_analyze.append(Letter(word[i],CORRECT_PLACE, i).toJson())
                else:
                    word_analyze.append(Letter(word[i],WRONG_PLACE, i).toJson())
            else:
                word_analyze.append(Letter(word[i], NOT_EXIST).toJson())
        return word_analyze

    def print_analyze(self, analyze):
        for letter in analyze:
            print(letter.__str__(),end="")
        print()
    
    def finish_game(self):
        print(FINISH_GAME.format(time() - self.start_time))

    def process_guess(self, word):
       
        if word == self.chosen_word:
            return True
        else:
            return self.analyze_word(word)            

    def run(self):
        while(True):
            guessed_word = input("Please enter your guess: ").lower().strip()
            guessed_word = validate_word(guessed_word)

            if guessed_word == self.chosen_word:
                print(YOU_WON)
                self.finish_game()
                break
            else:
                analyze = self.analyze_word(guessed_word)
                self.print_analyze(analyze)
                print(TRY_AGAIN)

            self.chance_count -= 1
            if self.chance_count == 0:
                print(YOU_LOST)
                self.finish_game()
                break

def main():
    game = Wordle()
    game.run()

if __name__ == "__main__":
    main()