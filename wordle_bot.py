from random import choice
from wordle import Wordle
from module.reader import get_words
from time import time
from config import CORRECT_PLACE, BOT_GUESSED_WORD, WRONG_PLACE, NOT_EXIST, YOU_LOST, YOU_WON, TRY_AGAIN

class WordleBot:

    def __init__(self,game=Wordle()):
        self.words = get_words()
        self.game = game
        self.chance_count = self.game.chance_count
        self.start_time = time()

    def process_analyze(self, analyze, new_word_list=[]):
        self.game.print_analyze(analyze)
        if new_word_list == []:
            new_word_list = self.words

        for value in analyze:
            if value.status == CORRECT_PLACE:
                new_word_list = self.get_words_correct_place(value, new_word_list)
            elif value.status == WRONG_PLACE:
                new_word_list = self.get_words_wrong_place(value, new_word_list)
            elif value.status == NOT_EXIST:
                new_word_list = self.get_words_not_exist(value, new_word_list)
            
        self.words = new_word_list

        return new_word_list

    def get_words_wrong_place(self, letter, words_list):
        new_list = []
        for word in words_list:
            if letter.value in word:
                if letter.value != word[letter.index]:
                    new_list.append(word)
        return new_list
    
    def get_words_correct_place(self, letter, words_list):
        new_list = []
        for word in words_list:
            if letter.value == word[letter.index]:
                new_list.append(word)
        return new_list

    def get_words_not_exist(self, letter, words_list):
        new_list = []
        for word in words_list:
            if letter.value not in word:
                new_list.append(word)
        return new_list

    def choose_word(self,words=None):
        if(words is None):
            words = self.words
        return choice(words)
        
    def simulate_game(self):
        guessed_word = self.choose_word()
        print(BOT_GUESSED_WORD.format(guessed_word))

        while(True):
            if guessed_word == self.game.chosen_word:
                print(YOU_WON)
                self.game.finish_game()
                break
            else:
                analyze = self.game.analyze_word(guessed_word)
                new_list = self.process_analyze(analyze)
                print(TRY_AGAIN)

            self.chance_count -= 1
            if self.chance_count == 0:
                print(YOU_LOST)
                self.game.finish_game()
                break

            guessed_word = self.choose_word(new_list)
            print(BOT_GUESSED_WORD.format(guessed_word))


def bot_game():
    bot = WordleBot()
    bot.simulate_game()

if __name__ == "__main__":
    bot_game()