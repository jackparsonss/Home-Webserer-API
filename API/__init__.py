from flask import Flask
from flask_restful import Api

def create_app():
    app = Flask(__name__)
    api = Api(app)

    from .views import Sensor

    api.add_resource(Sensor, '/api/get-data')

    return app