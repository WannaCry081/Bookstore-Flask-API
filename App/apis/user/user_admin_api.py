from App import DB
from App.utils import jwt_is_blacklist, admin_required
from App.models import (
    UserModel, 
    users_schema
)

from flask_jwt_extended import jwt_required
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
    @jwt_is_blacklist
    @admin_required
    def get(self):
        user = UserModel.query.all()
        schema = users_schema.dump(user)
        return schema, 200


    @jwt_required()
    @jwt_is_blacklist
    @admin_required
    def delete(self):
        
        data = self.parser.parse_args()

        user = UserModel.query.filter_by(
            id = data["id"], email = data["email"]
        ).first()

        if not user or user.id == 1:
            abort(404, message="User does not exists")

        DB.session.delete(user)
        DB.session.commit()

        return {"message" : f"User '{user.username}' successfully deleted"}


        
        