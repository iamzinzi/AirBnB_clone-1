#!/usr/bin/python3
"""Starts a Flask web application with routing"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Display a number only if it is an int"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
