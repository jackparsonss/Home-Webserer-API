from flask import Flask
from flask_restful import Api


def create_app():
    app = Flask(__name__, template_folder="../Website/templates")
    api = Api(app)

    from .API.views import Sensor, LEDToggle, views

    app.register_blueprint(views, url_prefix='/')

    api.add_resource(Sensor, '/api/get-data')
    api.add_resource(LEDToggle, '/api/led-<string:state>')

    return app
