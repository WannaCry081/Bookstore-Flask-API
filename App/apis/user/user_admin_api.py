from App.app import DB
from App.models import UserModel, UserBookModel

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)



class AdminUserResource(Resource):
    def __init__(self):
        pass


    def get(self):
        pass


    def delete(self):
        pass
