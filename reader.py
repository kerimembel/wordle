from config import DATA_FOLDER,WORDS,PREV_WORDS

def get_words():
    words = []
    with open(DATA_FOLDER + WORDS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words.append(line.strip().lower())
    return words
    
def get_previous_words():
    previous_words = []
    with open(DATA_FOLDER + PREV_WORDS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            previous_words.append(line.strip().lower())

    return previous_words

def get_available_words():
    words = get_words()
    previous_words = get_previous_words()

    for prev_word in previous_words:
        if prev_word in words:
            words.remove(prev_word)
    return words