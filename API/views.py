from flask import Blueprint, render_template
from flask_restful import Resource
from Data.get_data import get_data

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")


class Sensor(Resource):
    def get(self):
        data = get_data()
        return data
