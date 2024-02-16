#!/usr/bin/python3
from flask import Flask
"""a script that starts a Flask web application"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """a Methodthat writes HBNB on the web"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(debug=True)
