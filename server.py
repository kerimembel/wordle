from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from rest_response import GetUsernameResponse, HighScoreListResponse, RestResponse, Status, WordResponse, WordsResponse
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
    response = WordResponse(Status.OK, wordle.chosen_word)
    return jsonify(response.__dict__)

@app.route('/get-words', methods=['GET'])
@auth.login_required
def get_words():
    response = WordsResponse(Status.OK, list(wordle.words.keys()))
    return jsonify(response.__dict__)

@app.route('/highscore', methods=['GET'])
@auth.login_required
def get_highscores():
    response = HighScoreListResponse(Status.OK, wordle.get_highscores())
    return jsonify(response.__dict__)

@app.route('/highscore', methods=['POST'])
@auth.login_required
def add_highscore():
    data = request.get_json()
    username = data['username']
    score = float(data['score'])

    if not wordle.add_highscore(username, score):
        response = RestResponse(Status.HIGHSCORE_EXISTS)
        return jsonify(response.__dict__), 400
    else:
        response = RestResponse(Status.OK)
        return jsonify(response.__dict__)

@app.route('/get-username', methods=['GET'])
@auth.login_required
def get_username():
    client_id = request.args.get('client_id')

    if client_id is None:
        response = GetUsernameResponse(Status.CLIENT_ID_REQUIRED)
        return jsonify(response.__dict__), 400

    response = GetUsernameResponse(username = wordle.get_username(client_id))
    return jsonify(response.__dict__)

@app.route('/register-user', methods=['POST'])
@auth.login_required
def register_user():
    data = request.get_json()
    try:
        client_id = data['client_id']
    except KeyError:
        response = RestResponse(Status.CLIENT_ID_REQUIRED)
        return jsonify(response.__dict__), 400
    
    try:
        username = data['username']
    except KeyError:
        response = RestResponse(Status.USERNAME_REQUIRED)
        return jsonify(response.__dict__), 400

    if not wordle.register_user(client_id, username):
        response = RestResponse(Status.USERNAME_EXISTS)
        return jsonify(response.__dict__), 400
    else:
        response = RestResponse()
        return jsonify(response.__dict__), 201

@app.route('/update-username', methods=['POST'])
@auth.login_required
def update_username():

    data = request.get_json()
    try:
        client_id = data['client_id']
    except KeyError:
        response = RestResponse(Status.CLIENT_ID_REQUIRED)
        return jsonify(response.__dict__), 400
    
    try:
        username = data['username']
    except KeyError:
        response = RestResponse(Status.USERNAME_REQUIRED)
        return jsonify(response.__dict__), 400

    if not wordle.update_username(client_id, username):
        response = RestResponse(Status.USERNAME_EXISTS)
        return jsonify(response.__dict__), 400
    else:
        response = RestResponse()
        return jsonify(response.__dict__)


app.run(port=9000, host='0.0.0.0')