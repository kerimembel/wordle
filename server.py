from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from model.rest_response import HighScoreListResponse, HighScoreResponse, ValidateResponse, WordResponse, AnalyzeResponse
from wordle import Wordle
from module.validator import api_validate_word
from module.environment import get_env

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["DEBUG"] = True
wordle = Wordle()

users = {
    "kerim": generate_password_hash(get_env("PASSWORD_KERIM")),
    "onur": generate_password_hash(get_env("PASSWORD_ONUR"))
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/todays-word', methods=['GET'])
@auth.login_required
def get_word():
    response = WordResponse(True, wordle.chosen_word)
    return jsonify(response.__dict__)

@app.route('/validate-word', methods=['GET'])
@auth.login_required
def validate_word():
    word = request.args.get('word')
    response = ValidateResponse(wordle.validate_word(word), word)
    return jsonify(response.__dict__)

@app.route('/highscore', methods=['POST'])
@auth.login_required
def add_highscore():

    data = request.get_json()
    username = data['username']
    score = float(data['score'])

    if not wordle.add_highscore(username, score):
        response = HighScoreResponse(False, "This user already has a highscore")
    else:
        response = HighScoreResponse(True)

    return jsonify(response.__dict__)


@app.route('/highscore', methods=['GET'])
@auth.login_required
def get_highscores():
    response = HighScoreListResponse(True, wordle.get_highscores())
    return jsonify(response.__dict__)

@app.route('/analyze-word', methods=['GET'])
@auth.login_required
def analyze_word():
    word = request.args.get('word')

    if not api_validate_word(word):
        response = AnalyzeResponse(False, "")
        return response.toJson()
    else:
        word_analyze = wordle.analyze_word(word)
        response = AnalyzeResponse(True, word_analyze)

    return response.toJson()

app.run(port=9000)