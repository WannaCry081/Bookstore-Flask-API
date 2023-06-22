from App.app import DB
from sqlalchemy import func


class UserModel(DB.Model):
    __tablename__ = "users"

    id = DB.Column(DB.Integer, primary_key = True)

    username = DB.Column(DB.String(100), unique=True, nullable=False)
    email = DB.Column(DB.String(100), unique=True, nullable=False)
    password = DB.Column(DB.String(100), nullable=False)

    date = DB.Column(DB.DateTime, default=func.now())

    no_of_books = DB.Column(DB.Integer, default=0)


    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "email" : self.email,
            "username" : self.username,
            "No. of Books" : self.no_of_books
        }
    

    def __repr__(self) -> str:
        return "<User %r>"%self.username