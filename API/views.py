from flask import Flask
from flask_restful import Resource
from Data import get_data

class Sensor(Resource):
    def get(self):
        data = get_data
        return data
