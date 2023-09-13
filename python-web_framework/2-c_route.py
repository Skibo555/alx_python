#!/usr/bin/python3
"""
This is a script that directes a user to the home page of a site.
"""
from flask import Flask
from markupsafe import escapse

app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route("/")
def display():
    """
    This function directes visitors to my homepage.
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def display2():
    """
    This function is to bring my visitors to HBNB page, thanks to ALX!
    """
    return "HBNB"


@app.route('/c/<text>')
def display3(text):
    """
    This function returns the values of a dynamic route using flask!
    """
    text = text.replace('_', " ")
    return "C {}".format(escape(good))


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
