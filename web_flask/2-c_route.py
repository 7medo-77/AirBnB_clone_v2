#!/usr/bin/python3
"""
Flask instance with a routing to root
"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """
    Function which prints the phrase Hello HBNB!
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def holberton():
    """
    Function which prints the phrase HBNB
    """
    return ("HBNB")


@app.route('/<path:subpath>', strict_slashes=False)
def c_is(subpath):
    """
    Function which prints the phrase HBNB
    """
    text_list = subpath.split(sep='_')
    string_to_print = " ".join(text_list)
    return ("C {}".format(string_to_print))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
