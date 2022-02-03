from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()
cors = CORS()
jwt = JWTManager()


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object("config.Config")
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    with app.app_context():

        from .models import User, Profile, Dupe, World

        db.create_all()

        from . import auth

        app.register_blueprint(auth.bp)
