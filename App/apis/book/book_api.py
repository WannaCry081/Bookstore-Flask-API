from App.app import DB
from App.models import (
    BookModel,
    UserBookModel,
    UserModel
)

from flask_restful import (
    Resource, 
    reqparse,
    abort
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)



class BookResource(Resource):
    def get(self):
        pass


class BookDetailResource(Resource):
    def get(self, book_id : int, book_title : str):
        pass


class UserBookResource(Resource):
    def __init__(self):
        pass

    
    def get(self, user_id : int):
        pass


    def post(self, user_id : int):
        pass

    def delete(self, user_id : int):
        pass

