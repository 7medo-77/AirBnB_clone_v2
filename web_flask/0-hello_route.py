#!/usr/bin/python3
"""
Flask instance with a routing to root
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """
    Function which prints the phrase Hello HBNB!
    """
    return ("Hello HBNB!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
