from App.app import DB
from sqlalchemy import func


class BookModel(DB.Model):
    __tablename__ = "books"

    id = DB.Column(DB.Integer, primary_key = True)

    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))

    title = DB.Column(DB.String(100), unique=True, nullable=False)
    author = DB.Column(DB.String(100))
    genre = DB.Column(DB.String(100))
    description = DB.Column(DB.Text)
    price = DB.Column(DB.Numeric(5,2))
    date = DB.Column(DB.DateTime, default=func.now())

    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "genre" : self.genre,
            "description" : self.description,
            "price" : self.price
        }
    
    def __repr__(self) -> str:
        return "<Book %r>"%self.title

