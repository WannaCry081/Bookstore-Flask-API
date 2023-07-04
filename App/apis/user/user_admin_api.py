from App import DB
from App.models import (
    UserModel, 
    users_schema
)

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)
from flask_restful import (
    Resource,
    reqparse,
    abort
)



class AdminUserResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("id", type=int, required=True)
        self.parser.add_argument("email", type=str, required=True)

    @jwt_required()
    def get(self):
        identity = get_jwt_identity()

        user : UserModel = UserModel.query.filter_by(email = identity).first()
        if user.id != 1:
            abort(404, message="Page does not exists")

        user = UserModel.query.all()
        schema = users_schema.dump(user)
        return schema, 200

    @jwt_required()
    def delete(self):
        
        data = self.parser.parse_args()
        identity = get_jwt_identity()

        user : UserModel = UserModel.query.filter_by(email = identity).first()
        if user.id != 1:
            abort(404, message="Page does not exists")

        user = UserModel.query.filter_by(
            id = data["id"], email = data["email"]
        ).first()

        if not user or user.id == 1:
            abort(404, message="User does not exists")

        DB.session.delete(user)
        DB.session.commit()

        return {"message" : f"User '{user.username}' successfully deleted"}


        
        