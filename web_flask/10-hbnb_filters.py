#!/usr/bin/python3
"""Starts a Flask web application with HBNB clone"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(response_or_exc):
    """Removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_hbnb_filters():
    """Shows State and its Cities in HBNB filters website
    """
    data = storage.all('State')
    states = [v for k, v in data.items()]
    data = storage.all('Amenity')
    amenities = [v for k, v in data.items()]

    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
