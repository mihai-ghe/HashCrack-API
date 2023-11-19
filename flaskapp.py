# import flask module
from flask import Flask

# create instance of flask application
app = Flask(__name__)


# Send Hashes Endpoint
@app.route("/send")
def placeholder():

    return 1


@app.route("/status")
def placeholder1():

    return 1


@app.route("/check")
def placeholder2():

    return 1


@app.route("/reset")
def placeholder3():

    return 1
