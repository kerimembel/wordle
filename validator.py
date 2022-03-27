import re
from config import WORD_LENGHT
from reader import get_words

def validate_word(word):
    words = get_words()
    while not re.match("^[A-Za-z]*$", word):
        print ("Error! Make sure you only use letters in your guess")
        word = input("Please enter your guess: ")
   
    while not len(word) == WORD_LENGHT:
        print ("Error! Make sure you only use {} letters in your guess".format(WORD_LENGHT))
        word = input("Please enter your guess: ")
    
    while not word in words:
        print ("Error! Please enter a valid word")
        word = input("Please enter your guess: ")

    return word