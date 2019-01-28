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


@app.route('/c/<text>', strict_slashes=False)
def say_c_text(text):
    """Displays C followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "c {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def say_python_text(text='is cool'):
    """Display Python followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
