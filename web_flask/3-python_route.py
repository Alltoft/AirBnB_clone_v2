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


@app.route("/c/<name>", strict_slashes=False)
def c(name):
    """a Methodthat writes C + {name} message"""
    new_name = name.replace("_", " ")
    return "C {}".format(new_name)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """a Methodthat writes python + {text} message"""
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
