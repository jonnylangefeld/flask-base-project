import requests
import re

from datetime import datetime, timedelta
from json import dumps, load, loads

from flask import Flask, render_template, Response

def sample_function():
    """This is a sample docstring subject

    This is a sample docstring description.

    Args:
        s (str): a string argument
        i (int): an integer argument

    Returns:
         dict: a dictionary is returned

    Raises:
        Any exception to be caught later.
    """
    return "Hello World"


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Return the index.html page"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
