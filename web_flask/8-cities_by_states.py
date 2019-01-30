#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(response_or_exc):
    """Removes the current SQLAlchemy Session
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_states():
    """Shows all Cities by State instances
    """
    data = storage.all('State')
    states = []
    for k, v in data.items():
        states.append(v)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
