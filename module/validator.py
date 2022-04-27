import re
from config import WORD_LENGHT
from .reader import get_words

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

def api_validate_word(word):
    status = True
    words = get_words()
    if not re.match("^[A-Za-z]*$", word):
        status = False
        print("Error! Make sure you only use letters in your guess")

    if not len(word) == WORD_LENGHT:
        status = False
        print("Error! Make sure you only use {} letters in your guess".format(WORD_LENGHT))

    if not word in words:
        status = False
        print("Error! Please enter a valid word")

    return status