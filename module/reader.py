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

def clear_words():
    words_list = []
    with open(DATA_FOLDER + WORDS, 'r') as file:
        lines = file.readlines()
        for line in lines:
            word = line.strip().lower()
            if word not in words_list:
                words_list.append(word)
    
    with open(DATA_FOLDER + WORDS, 'w') as file:
        for word in words_list:
            file.write(word + "\n")

def sort_words():
    all_words = get_words()
    sorted_words = sorted(all_words)
    with open(DATA_FOLDER + WORDS, 'w') as file:
        for word in sorted_words:
            file.write(word + "\n")


if __name__== "__main__":
    sort_words()