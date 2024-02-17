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


@app.route("/states/<id>", strict_slashes=False)
def display_by_id(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state, id=id)
    return render_template('9-states.html', state=state, id=id)


@app.route("/states", strict_slashes=False)
def display():
    """a method to display an html file"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
