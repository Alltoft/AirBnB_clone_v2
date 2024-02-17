#!/usr/bin/python3
"""a script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """render states, amenities and places in the route"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template(
        "100-hbnb.html",
        states=states,
        amenities=amenities,
        places=places,
    )


@app.teardown_appcontext
def close_storage(exception):
    """Close sqlalchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
