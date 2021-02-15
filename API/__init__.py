from flask import Flask
from flask_restful import Api
from gpiozero import LED

def create_app():
    app = Flask(__name__, template_folder="../templates")
    api = Api(app)
    led = LED(2)
    led.off()

    from .views import Sensor, views

    app.register_blueprint(views, url_prefix='/')

    api.add_resource(Sensor, '/api/get-data')

    return app