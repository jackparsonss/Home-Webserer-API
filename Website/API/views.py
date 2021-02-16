from flask import Blueprint, render_template
from flask_restful import Resource
from Website.Data.get_data import get_data

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("fetchData.html")


class Sensor(Resource):
    def get(self):
        data = get_data()
        return data
