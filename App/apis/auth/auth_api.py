from App.models import UserModel, TokenModel
from App.utils import isValidEmail
from App import BCRYPT, DB

from flask_restful import (
    Resource,
    reqparse,
    abort
)
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    get_jwt
)


class SignUpResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)

    def post(self):

        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(
            username = data["username"], email = data["email"]
        ).first()

        if user: 
            abort(401, message = "User already exits")

        if len(data["username"]) < 4:
            abort(401, message="Username must at least be 4 characters long")
            
        if not isValidEmail(data["email"]):
            abort(401, message="Invalid email address")

        if len(data["password"]) < 6:
            abort(401, "Password must at least be 6 characters long")

        user = UserModel(
            username = data["username"],
            email = data["email"],
            password = BCRYPT.generate_password_hash(data["password"])
        )

        access_token = create_access_token(identity = user.email)
        refresh_token = create_refresh_token(identity = user.email)

        DB.session.add(user)
        DB.session.commit()

        return {    
            "access_token" : access_token,
            "refresh_token" : refresh_token,
            "user" : user.toObject(),
            "message" : "User successfully created"
        }, 200


class SignInResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("email", type=str, required=True)
        self.parser.add_argument("password", type=str, required=True)

    def post(self):
        data = self.parser.parse_args()

        user : UserModel = UserModel.query.filter_by(email = data["email"]).first()
        if user:
            if not BCRYPT.check_password_hash(user.password, data["password"]):
                abort(401, message="Incorrect password")

            access_token = create_access_token(identity=user.email)
            refresh_token = create_refresh_token(identity=user.email)

            return {
                "access_token" : access_token,
                "refresh_token" : refresh_token,
                "user" : user.toObject(),
                "message" : "Access Authorized"
            }, 200

        else:
            abort(404, message="User does not exists")


class SignOutResource(Resource):

    @jwt_required(optional=True)
    def post(self):
        try:
            jti = get_jwt()["jti"]
            revoked_token = TokenModel(token = jti)

            DB.session.add(revoked_token)
            DB.session.commit()

            return {"message" : "Logged out successfully"}, 200
        except Exception as e:
            abort(500, message=e)


class RefreshTokenResource(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if not user:
            abort(404, message="User does not exists")

        new_token = create_access_token(identity=access_token)
        return {"access_token" : new_token}, 200


class RefreshSignOutResource(Resource):

    @jwt_required(refresh=True)
    def post(self):
        try:
            jti = get_jwt()["jti"]
            revoked_token = TokenModel(token = jti)

            DB.session.add(revoked_token)
            DB.session.commit()

            return {"message" : "Logged out successfully"}, 200
        except Exception as e:
            abort(500, message=e)
