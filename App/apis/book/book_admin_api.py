from App import DB
from App.utils import jwt_is_blacklist, admin_required
from App.models import (
    UserModel,
    BookModel
)

from flask_restful import Resource, reqparse, abort
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


class AdminBookResource(Resource):
    def __init__(self):
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument("title", type=str, required=True)
        self.post_parser.add_argument("author", type=str, required=True)
        self.post_parser.add_argument("genre", type=str, required=True)
        self.post_parser.add_argument("description", type=str, required=True)
        self.post_parser.add_argument("price", type=float, required=True)
        
        self.put_parser = reqparse.RequestParser()
        self.put_parser.add_argument("title", type=str, required=True)
        self.put_parser.add_argument("description", type=str, required=True)
        self.put_parser.add_argument("price", type=float, required=True)
        
        self.delete_parser = reqparse.RequestParser()
        self.delete_parser.add_argument("id", type=int, required=True) 
        self.delete_parser.add_argument("title", type=str, required=True) 


    @jwt_required()
    @jwt_is_blacklist
    @admin_required
    def post(self):
        data = self.post_parser.parse_args()

        book : BookModel = BookModel.query.filter_by(title = data["title"]).first()
        if book:
            abort(404, message="Book already exists")

        book = BookModel(
            title = data["title"],
            author = data["author"],
            genre = data["genre"],
            description = data["description"],
            price = data["price"]
        )
    
        DB.session.add(book)
        DB.session.commit()

        return {"message" : "Successfully created"}, 200
     
    @jwt_required()
    @jwt_is_blacklist
    @admin_required
    def put(self):
        data = self.put_parser.parse_args()
      
        book : BookModel = BookModel.query.filter_by( title = data["title"]).first()
        if not book:
            abort(404, message="Book does not exists")

        if data["description"]:
            book.description = data["description"]

        if data["price"]:
            book.price = data["price"]

        DB.session.commit()
        return {"message" : "Successfully updated"}, 200


    @jwt_required()
    @jwt_is_blacklist
    @admin_required
    def delete(self):
        
        data = self.delete_parser.parse_args()
        
        book : BookModel = BookModel.query.filter_by(
            id = data["id"], title = data["title"]
        ).first()

        if not book:
            abort(404, message="Book does not exists")
        
        DB.session.delete(book)
        DB.session.commit()
        return {"message" : f"Book '{book.title}' successfully deleted"}, 200
        