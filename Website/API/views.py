from flask import Blueprint, render_template
from flask_restful import Resource
from Website.Data.utils import get_data, toggle_led

views = Blueprint('views', __name__)

# Frontend Views
@views.route('/')
def home():
    return render_template("fetchData.html")

@views.route('/LED')
def LED():
    return render_template("toggleLED.html")

# API Views
class Sensor(Resource):
    def get(self):
        data = get_data()
        return data

class LEDToggle(Resource):
    def get(self, state):
        return toggle_led(state)

