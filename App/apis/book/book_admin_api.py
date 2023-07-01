from App.app import DB
from App.models import (
    UserModel,
    BookModel,
    UserBookModel
)

from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class AdminBookResource(Resource):
    def __init__(self):
        pass


    def put(self):
        pass

    
    def post(self):
        pass


    def delete(self):
        pass