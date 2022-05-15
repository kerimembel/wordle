from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from rest_response import HighScoreListResponse, HighScoreResponse, WordResponse, WordsResponse
from environment import get_env
from wordle import Wordle

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

@app.route('/get-words', methods=['GET'])
@auth.login_required
def get_words():
    response = WordsResponse(True, list(wordle.words.keys()))
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

app.run(port=9000)