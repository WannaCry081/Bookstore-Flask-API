from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS

import json


DB : SQLAlchemy = SQLAlchemy()
JWT : JWTManager = JWTManager()
BCRYPT : Bcrypt = Bcrypt()
MALLOW : Marshmallow = Marshmallow()


def create_bookstore_app(environment) -> Flask:

    my_app : Flask = Flask(__name__)
    my_app.config.from_object(environment)

    API : Api = Api(my_app)
    DB.init_app(my_app)
    JWT.init_app(my_app)
    BCRYPT.init_app(my_app)
    MALLOW.init_app(my_app)
    CORS(my_app)


    from App.apis.auth import (
        SignInResource,
        SignOutResource,
        SignUpResource,
        RefreshSignOutResource,
        RefreshTokenResource
    )
    from App.apis.user import (
        UserResource,
        AdminUserResource
    )
    from App.apis.book import (
        BookResource,
        BookDetailResource,
        UserBookResource,
        AdminBookResource
    )


    API.add_resource(SignInResource, "/api/auth/signin")
    API.add_resource(SignUpResource, "/api/auth/signup")
    API.add_resource(SignOutResource, "/api/auth/signout")
    API.add_resource(RefreshTokenResource, "/api/auth/refresh")
    API.add_resource(RefreshSignOutResource, "/api/auth/refresh/signout")

    API.add_resource(UserResource, "/api/user/<int:user_id>")

    API.add_resource(BookResource, "/api/book")
    API.add_resource(BookDetailResource, "/api/book/<int:book_id>/<book_title>")
    API.add_resource(UserBookResource, "/api/book/user/<int:user_id>")

    API.add_resource(AdminUserResource, "/api/admin/user")
    API.add_resource(AdminBookResource, "/api/admin/book")
    

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