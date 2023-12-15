# import flask module
from flask import Flask
from flask import request

import DB_Methods

# create instance of flask application
app = Flask(__name__)


# Send Hashes to the DB
@app.route("/send", methods=["POST"])
def send():

    key = request.authorization.token

    user_data = DB_Methods.check_key(key)

    if not user_data:

        return "<h> Nope </h>", 401

    json = request.json

    DB_Methods.enter_hash(json['hash'], json['format'], user_data[0][0])

    return "<h> Yep </h>", 201


# Get status of ongoing cracking threads
@app.route("/status", methods=['GET'])
def status():

    return 1


# Check whether the respective hash has an entry in the DB
@app.route("/check", methods=['GET'])
def check():

    return 1


@app.route("/display_all", methods=['GET'])
def display_all():

    return 1


@app.route("/start", methods=['PUT'])
def start():

    return 1


# Terminate a cracking thread
@app.route("/end", methods=['PUT'])
def end():

    return 1
