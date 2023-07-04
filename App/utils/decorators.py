from App.models import TokenModel, UserModel
from flask_restful import abort
from flask_jwt_extended import get_jwt, get_jwt_identity


def jwt_is_blacklist(func):
    def wrapper(*args, **kwargs):

        access_token = get_jwt()["jti"]    
        token : TokenModel = TokenModel.query.filter_by(token=access_token).first()
        if token:
            abort(401, message="Token is blacklisted")
        
        return func(*args, **kwargs)
    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):

        user_id = kwargs.get("user_id")
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User does not exists")

        return func(*args, **kwargs)
    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):

        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()
        if user.id == 1:
            return func(*args, **kwargs)
        
        abort(404, message="Page does not exists")
    return wrapper