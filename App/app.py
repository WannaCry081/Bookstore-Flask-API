from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from App.config import Config

import json


DB : SQLAlchemy = SQLAlchemy()
JWT : JWTManager = JWTManager()
BCRYPT : Bcrypt = Bcrypt()
MALLOW : Marshmallow = Marshmallow()


def create_bookstore_app(config_class : Config = Config) -> Flask:

    my_app : Flask = Flask(__name__)
    my_app.config.from_object(config_class)

    API : Api = Api(my_app)
    DB.init_app(my_app)
    JWT.init_app(my_app)
    BCRYPT.init_app(my_app)
    MALLOW.init_app(my_app)
    CORS(my_app)


    from App.apis.auth import AUTH_API
    from App.apis.user import USER_API, USER_ADMIN_API
    from App.apis.book import BOOK_API, BOOK_ADMIN_API


    # my_app.register_blueprint(AUTH_API, url_prefix="/api/auth/")
    # my_app.register_blueprint(USER_API, url_prefix="/api/user/")
    # my_app.register_blueprint(USER_ADMIN_API, url_prefix="/api/admin/user/")
    # my_app.register_blueprint(BOOK_API, url_prefix="/api/book/")
    # my_app.register_blueprint(BOOK_ADMIN_API, url_prefix="/api/admin/book/")




    with my_app.app_context():
        DB.create_all()
        load_book_list()

    return my_app


def load_book_list() -> None:
    """
    Inserting preloaded books in the `books` table for user manipulation
    you can also add books in the `App/static/json/books.json` 
    """
    from App.models import BookModel

    with open("App/static/json/books.json", "r") as file:
        books = json.load(file)
    
        for data in books:
            book : BookModel = BookModel.query.filter_by(title = data["title"]).first()
            if not book:
                DB.session.add(BookModel(
                    title = data["title"],
                    author = data["author"],
                    genre = data["genre"],
                    description = data["description"],
                    price = data["price"]
                ))
                DB.session.commit()
            else:
                continue
    
        file.close()
    return