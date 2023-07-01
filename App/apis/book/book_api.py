from App.app import DB
from App.models import (
    BookModel,
    UserBookModel,
    UserModel, 
    books_schema,
    book_schema
)

from flask_jwt_extended import jwt_required
from flask_restful import (
    Resource, 
    reqparse,
    abort
)


class BookResource(Resource):
    def get(self):
        books : BookModel = BookModel.query.all()   
        schema = books_schema.dump(books)
        return {"books" : schema }


class BookDetailResource(Resource):
    def get(self, book_id : int, book_title : str):
        book : BookModel = BookModel.query.filter_by(
            id = book_id, title = book_title
        ).first()

        if not book:
            abort(404, message="Book does not exists")

        schema = book_schema.dump(book)
        return schema, 200


class UserBookResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("title", type=str, required=True)
        
    @jwt_required()
    def get(self, user_id : int):
        
        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User does not exists")

        book_list = []
        userBooks : UserBookModel = UserBookModel.query.filter_by(user_id = user_id).all()

        for userBook in userBooks:
            book_list.append(book_schema.dump(BookModel.query.get(userBook.id)))

        return {"books" : book_list}, 200

    @jwt_required()
    def post(self, user_id : int):
        title = self.parser.parse_args()["title"]

        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User does not exists")

        book : BookModel = BookModel.query.filter_by(title=title).first()
        if not book:
            abort(404, message="Book does not exists")


        user.no_of_books = int(user.no_of_books) + 1
        userBook : UserBookModel = UserBookModel(
            user_id = user.id,
            book_id = book.id
        )

        DB.session.add(userBook)
        DB.session.commit()

        return {"message" : "Successfully added book"}, 200

    @jwt_required()
    def delete(self, user_id : int):
        title = self.parser.parse_args()["title"]

        user : UserModel = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User does not exists")

        book : BookModel = BookModel.query.filter_by(title=title).first()
        if not book:
            abort(404, message="Book does not exists")

        user.no_of_books = int(user.no_of_books) -1
        userBook : UserBookModel = UserBookModel.query.filter_by(
            user_id = user.id, book_id = book.id
        ).first()
        
        DB.session.delete(userBook)
        DB.session.commit()

        return {"message" : "Successfully deleted book"}, 200
