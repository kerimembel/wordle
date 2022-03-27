from config import DATA_FOLDER, PREV_WORDS

def record_current_word(word):
    with open(DATA_FOLDER + PREV_WORDS, 'a') as f:
        f.write(word + '\n')
    