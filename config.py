class Config:
    # SQLALCHEMY config
    SQLALCHEMY_DATABASE_URI = "sqlite:///oni-planning.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT config
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_COOKIE_NAME = "access_token_cookie"
