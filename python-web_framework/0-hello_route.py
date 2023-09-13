#!/usr/bin/python3
"""
This is a script that directes a user to the home page of a site.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def display():
    print("Hello HBNB!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, strict_slashes=False)
