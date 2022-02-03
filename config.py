import os
from datetime import timedelta


class Config:

    SECRET_KEY = os.environ["SECRET_KEY"]

    # SQLALCHEMY config
    SQLALCHEMY_DATABASE_URI = "sqlite:///oni-planning.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT config
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_COOKIE_NAME = "access_token_cookie"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=6)
