from App.app import DB, BCRYPT
from App.models import UserModel, UserBookModel

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource, 
    reqparse,
    abort
)


class UserResource(Resource):
    def __init__(self):
        pass

    @jwt_required()
    def get(self, user_id : int):
        pass


    @jwt_required()
    def post(self, user_id : int):
        pass


    @jwt_required()
    def put(self, user_id : int):
        pass


    @jwt_required()
    def delete(self, user_id : int):
        pass

