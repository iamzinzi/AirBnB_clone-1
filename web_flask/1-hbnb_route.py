#!/usr/bin/python3
"""Starts a Flask web application with routing"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    """Displays message for HBNB home page"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def say_hbnb():
    """Displays message for /hbnb"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
