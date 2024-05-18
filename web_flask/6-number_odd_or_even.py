#!/usr/bin/python3
"""
Flask instance with a routing to root
"""
from flask import Flask
from flask import render_template
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


@app.route('/c/<path:subpath>', strict_slashes=False)
def c_is(subpath):
    """
    Function which prints the phrase HBNB
    """
    text_list = subpath.split(sep='_')
    string_to_print = " ".join(text_list)
    return ("C {}".format(string_to_print))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Function which prints the phrase HBNB
    """
    text_list = text.split(sep='_')
    string_to_print = " ".join(text_list)
    return ("Python {}".format(string_to_print))


@app.route('/number/<int:number>', strict_slashes=False)
def number(number):
    """
    Function which prints the phrase HBNB
    """
    return ("{} is a number".format(number))


@app.route('/number_template/<int:number>', strict_slashes=False)
def n(number):
    """
    Function which prints the phrase HBNB
    """
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>', strict_slashes=False)
def odd_or_even(number):
    """
    Function which prints the phrase HBNB
    """
    if (number % 2 == 0):
        parity = 'even'
    else:
        parity = 'odd'
    return render_template('6-number_odd_or_even.html',
                           number=number, parity=parity)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
