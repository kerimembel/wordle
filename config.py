class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

DATA_FOLDER = "data/"
PREV_WORDS = "previousWords.txt"
WORDS = "words.txt"

WORD_LENGHT = 5

CORRECT_PLACE = "G"
WRONG_PLACE = "Y"
NOT_EXIST = "B"

YOU_WON = bcolors.OKGREEN + "You won!" + bcolors.ENDC
YOU_LOST = bcolors.FAIL + "You lost!" + bcolors.ENDC
TRY_AGAIN = bcolors.WARNING + "Try again!" + bcolors.ENDC
FINISH_GAME = bcolors.OKBLUE + "You finished the game in {:.2f} seconds" + bcolors.ENDC
GUESSED_WORD = "Your guessed word is: "+bcolors.BOLD +"{}" + bcolors.ENDC
BOT_GUESSED_WORD = "Bot guessed the word : "+bcolors.BOLD +"{}" + bcolors.ENDC
CHOSEN_WORD = bcolors.OKCYAN + "The chosen word is: "+bcolors.BOLD+"{}" + bcolors.ENDC