from App.app import DB, MALLOW
from marshmallow import fields


class UserModel(DB.Model):
    __tablename__ = "users"

    id = DB.Column(DB.Integer, primary_key = True)

    username = DB.Column(DB.String(100), unique=True, nullable=False)
    email = DB.Column(DB.String(100), unique=True, nullable=False)
    password = DB.Column(DB.String(100), nullable=False)
    bio =  DB.Column(DB.Text)

    date = DB.Column(DB.Date, default=DB.func.current_date())
    no_of_books = DB.Column(DB.Integer, default=0)

    user_book = DB.relationship("UserBookModel")


    def __init__(self, username : str, email : str, password : str):
        self.username = username
        self.email = email
        self.password = password
        
    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "email" : self.email,
            "username" : self.username,
            "No. of Books" : self.no_of_books,
            "bio" :self.bio
        }
    

    def __repr__(self) -> str:
        return "<User %r>"%self.username
    

class UserSchema(MALLOW.Schema):

    class Meta:
        model : UserModel = UserModel
        fields : tuple = ("id", "username", "email", "bio", "no_of_books")

    id = fields.Integer()
    username = fields.String()
    email = fields.String()
    bio = fields.String()
    no_of_books = fields.Integer()


user_schema : UserSchema = UserSchema()
users_schema : UserSchema = UserSchema(many=True)