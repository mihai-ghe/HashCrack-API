# import flask module
from flask import Flask

# create instance of flask application
app = Flask(__name__)


# Send Hashes to the DB and start cracking
@app.route("/send", 'POST')
def placeholder():

    return 1


# Get status of ongoing cracking threads
@app.route("/status", 'GET')
def placeholder1():

    return 1


# Check whether the respective hash has an entry in the DB
@app.route("/check", 'GET')
def placeholder2():

    return 1


# Terminate a cracking thread
@app.route("/end", 'PUT')
def placeholder3():

    return 1
