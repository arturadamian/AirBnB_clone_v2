#!/usr/bin/python3
"""
starts a Flask web application
"""


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
