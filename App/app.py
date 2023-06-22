from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from App.config import Config


DB : SQLAlchemy = SQLAlchemy()
BCRYPT : Bcrypt = Bcrypt()
JWT : JWTManager = JWTManager()


def create_bookstore_app(config_class : Config = Config) -> Flask:

    my_app : Flask = Flask(__name__)
    my_app.config.from_object(config_class)
    
    CORS(my_app)
    DB.init_app(my_app)
    JWT.init_app(my_app)
    BCRYPT.init_app(my_app)


    from App.apis.auth import AUTH_API
    from App.apis.user import USER_API, USER_ADMIN_API
    from App.apis.book import BOOK_API, BOOK_ADMIN_API


    my_app.register_blueprint(AUTH_API, url_prefix="/api/auth/")
    my_app.register_blueprint(USER_API, url_prefix="/api/user/")
    my_app.register_blueprint(USER_ADMIN_API, url_prefix="/api/admin/user/")
    my_app.register_blueprint(BOOK_API, url_prefix="/api/book/")
    my_app.register_blueprint(BOOK_ADMIN_API, url_prefix="/api/admin/book/")


    from App.models import (
        UserModel,
        BookModel
    )

    with my_app.app_context():
        DB.create_all()

    return my_app
