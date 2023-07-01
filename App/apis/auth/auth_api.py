from App.models import UserModel
from App.app import BCRYPT, DB
from App.utils.validity import isValidEmail

from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)


class SignUpResource(Resource):
    pass


class SignInResource(Resource):
    pass


class SignOutResource(Resource):
    pass


class RefreshTokenResource(Resource):
    pass


class RefreshSignOutResource(Resource):
    pass

