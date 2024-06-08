#!/usr/bin/python3
"""
Flask instance with a routing to root
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
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


@app.route("/states_list", strict_slashes=False)
def display_states():
    """Render state_list html page to display States created"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_state():
    """Render state_list html page to display States created"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states", strict_slashes=False)
def state():
    """Render state_list html page to display States created"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/<string:id>", strict_slashes=False)
def state_cities(id):
    """Render state_list html page to display States created"""
    state = storage.get("State", id)
    if state:
        cities = state.cities
    else:
        cities = None
    return render_template('9-states.html', state=state, cities=cities)


@app.route("/hbnb_filters", strict_slashes=False)
def template():
    """Render hbnb Template"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close(self):
    """
    Method to remove current session
    """
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
