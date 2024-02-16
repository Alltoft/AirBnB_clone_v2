#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def session_close(exception):
    """a method to terminate a session"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display():
    """a method to dsplay an html file"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
