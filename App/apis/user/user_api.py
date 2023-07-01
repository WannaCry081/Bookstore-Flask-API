from App.app import DB, BCRYPT
from App.models import UserModel, UserBookModel

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    unset_jwt_cookies,
    unset_access_cookies
)


class UserResource(Resource):
    def __init__(self):
        pass


    def get(self, user_id : int):
        pass


    def post(self, user_id : int):
        pass


    def put(self, user_id : int):
        pass


    def delete(self, user_id : int):
        pass

