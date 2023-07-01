from App.app import DB, MALLOW
from marshmallow import fields


class UserBookModel(DB.Model):
    __tablename__ = "user_books"

    id = DB.Column(DB.Integer, primary_key = True)

    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))
    book_id = DB.Column(DB.Integer, DB.ForeignKey("books.id"))


    def __repr__(self) -> str:
        return "<UserBooks %r>"%self.id


class UserBookSchema(MALLOW.Schema):

    class Meta:
        model : UserBookModel = UserBookModel
        fields : tuple = ("id", "user_id", "book_id") 


userbook_schema : UserBookSchema = UserBookSchema()
userbooks_schema : UserBookSchema = UserBookSchema(many=True)