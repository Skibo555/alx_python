#!/usr/bin/python3
"""
This is a script that directes a user to the home page of a site.
"""
from flask import Flask, render_template
from markupsafe import escape

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


@app.route('/c/<good>')
def display3(good):
    """
    This function returns the values of a dynamic route using flask!
    """
    good = good.replace('_', " ")
    return "C {}".format(escape(good))


@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def display4(text):
    """
    This function displays a defualt.
    """
    text = text.replace('_', " ")
    return "Python {}".format(escape(text))


@app.route('/number/<int:n>')
def display5(n):

    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def display6(n):

    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
