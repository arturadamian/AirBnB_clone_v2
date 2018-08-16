#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello method"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display method"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_var(text):
    """display variable"""
    return 'C %s' % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_bydefault(text="is cool"):
    """display variable by default"""
    return 'Python %s' % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """display variable int"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_html(n):
    """rendering html"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
