#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """index"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cis_fun(text):
    """hbnb"""
    s = escape(text)
    s = s.replace("_", " ")
    return f"C {s}"


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)