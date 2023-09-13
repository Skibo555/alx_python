#!/usr/bin/python3
"""
This is a script that directes a user to the home page of a site.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def display():
    return "Hello HBNB!"
# app.run(strict_slashes=False)
