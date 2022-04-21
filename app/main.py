from flask import Flask
import os
import datetime


def create_app():
    app = Flask(__name__)

    from .views import greeting_bp
    app.register_blueprint(greeting_bp)

    return app
