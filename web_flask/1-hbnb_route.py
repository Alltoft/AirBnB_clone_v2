#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """a Methodthat writes HBNB on the web"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display():
    """a Methodthat writes HBNB message"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
