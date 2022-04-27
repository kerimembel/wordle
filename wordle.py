from random import choice
from module.reader import get_available_words
from module.writer import record_current_word
from module.validator import validate_word
from time import time
from config import CHOSEN_WORD, FINISH_GAME, NOT_EXIST, CORRECT_PLACE, WRONG_PLACE, YOU_LOST, YOU_WON, TRY_AGAIN
from model.letter import Letter

class Wordle():

    def __init__(self,chance_count=6):
        self.chosen_word = self.choose_word()
        self.chance_count = chance_count
        self.start_time = time()
    
    def choose_word(self):
        words = get_available_words()
        chosen_word = choice(words)
        record_current_word(chosen_word)
        #print(CHOSEN_WORD.format(chosen_word))
        return chosen_word.lower()

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