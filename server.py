from time import sleep
from flask import Flask, request
from model.rest_response import HighScoreListResponse, HighScoreResponse, ValidateResponse, WordResponse, AnalyzeResponse
from wordle import Wordle
from module.validator import api_validate_word

app = Flask(__name__)
app.config["DEBUG"] = True
wordle = Wordle()

@app.route('/', methods=['GET'])
def home():
    return "what's up"

@app.route('/todays-word', methods=['GET'])
def get_word():
    response = WordResponse(True, wordle.chosen_word)
    return response.toJson()

@app.route('/validate-word', methods=['GET'])
def validate_word():
    word = request.args.get('word')
    response = ValidateResponse(wordle.validate_word(word), word)
    return response.toJson()

@app.route('/highscore', methods=['POST'])
def add_highscore():

    data = request.get_json()
    username = data['username']
    score = data['score']

    wordle.add_highscore(username, score)
    response = HighScoreResponse(True, score, username)
    return response.toJson()


@app.route('/highscore', methods=['GET'])
def get_highscores():
    response = HighScoreListResponse(True, wordle.get_highscores())
    return response.toJson()

@app.route('/analyze-word', methods=['GET'])
def analyze_word():
    word = request.args.get('word')

    if not api_validate_word(word):
        response = AnalyzeResponse(False, "")
        return response.toJson()
    else:
        word_analyze = wordle.analyze_word(word)
        response = AnalyzeResponse(True, word_analyze)
        for analyze in word_analyze:
            print(analyze)

    return response.toJson()

app.run(port=9000)