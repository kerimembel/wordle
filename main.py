from wordle import Wordle
from wordle_bot import WordleBot

def player_game():
    game = Wordle()
    game.run()

def bot_game():
    bot = WordleBot()
    bot.simulate_game()

player_game()