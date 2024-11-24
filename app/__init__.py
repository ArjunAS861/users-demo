from flask import Flask, url_for
from flask_marshmallow import Marshmallow

from app.controllers.user_controller import user_blueprint
from app.db import db

ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(user_blueprint)

    return app