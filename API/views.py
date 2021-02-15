from flask import Blueprint
from flask_restful import Resource
from Data.get_data import get_data

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>This Detects the Temperature and Humidity of my Room</h1>"


class Sensor(Resource):
    def get(self):
        data = get_data()
        return data
