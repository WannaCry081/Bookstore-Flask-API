from App.app import DB, BCRYPT
from App.models import (
    UserModel,
    UserBookModel,
    user_schema
)

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource, 
    reqparse,
    abort
)


class UserResource(Resource):
    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument("old_password", type=str, required=True)
        self.post_parser.add_argument("new_password", type=str, required=True)
        
        self.put_parser = reqparse.RequestParser()
        self.put_parser.add_argument("username", type=str, required=True)
        self.put_parser.add_argument("bio", type=str, required=True)

    @jwt_required()
    def get(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            abort(404, message="User does not exists")

        schema = user_schema.dump(user)
        return schema, 200


    @jwt_required()
    def post(self, user_id : int):
        
        data = self.post_parser.parse_args()

        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            abort(404, message="User does not exists")
            
        if not BCRYPT.check_password_hash(user.password, data["old_password"]):
            abort(401, message="Incorrect password")

        if len(data["old_password"]) < 6:
            abort(401, message="Password must at least be 6 characters long")

        user.password = BCRYPT.generate_password_hash(data["old_password"])
        DB.session.commit()

        return {"message" : "Successfully updated password"}, 200


    @jwt_required()
    def put(self, user_id : int):
        
        data = self.put_parser.parse_args()
        
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            abort(404, message="User does not exists")
       
        if data["username"]:
            if len(data["username"]) < 4:
                abort(401, message="Username must at least be 4 characters long")

            user.username = data["username"]
        
        user.bio = data["bio"]
        DB.session.commit()

        return {"message" : "Successfully updated user"}, 200
    

    @jwt_required()
    def delete(self, user_id : int):
        user : UserModel = UserModel.query.filter_by(id = user_id).first()
        if not user:
            abort(404, message="User does not exists")
        
        userBooks : UserBookModel = UserBookModel.query.filter_by(user_id = user.id).all()
        if userBooks:
            DB.session.delete(userBooks)

        DB.session.delete(user)
        DB.session.commit()

        return {"message" : "Successfully deleted user"}, 200
