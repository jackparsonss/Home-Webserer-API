from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__, template_folder="../Website/templates")
    api = Api(app)

    from .API.views import Sensor, views

    app.register_blueprint(views, url_prefix='/')

    api.add_resource(Sensor, '/api/get-data')

    return app
