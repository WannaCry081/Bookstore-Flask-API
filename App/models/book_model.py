from App import DB, MALLOW
from marshmallow import fields


class BookModel(DB.Model):
    __tablename__ = "books"

    id = DB.Column(DB.Integer, primary_key = True)
    title = DB.Column(DB.String(100), unique=True, nullable=False)
    author = DB.Column(DB.String(100), nullable=False)
    genre = DB.Column(DB.String(100), nullable=False)
    description = DB.Column(DB.Text)
    price = DB.Column(DB.Numeric(5,2), default=0.00)
    date = DB.Column(DB.Date, default=DB.func.current_date())

    user_book = DB.relationship("UserBookModel")

    def __init__(self, title : str, author : str, genre : str, description : str, price : float):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description
        self.price = price 
    
    def __repr__(self) -> str:
        return "<Book %r>"%self.title

    def toObject(self) -> dict:
        return {
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "genre" : self.genre,
            "description" : self.description,
            "price" : self.price
        }
    

class BookSchema(MALLOW.Schema):

    class Meta:
        model : BookModel = BookModel
        fields : tuple = ("id", "title", "author", "genre", "description",
                            "price", "date")

    id = fields.Integer()
    title = fields.String()
    author = fields.String()
    description = fields.String()
    genre = fields.String() 
    description = fields.String()
    price = fields.Number()
    date = fields.Date()


book_schema : BookSchema = BookSchema()
books_schema : BookSchema = BookSchema(many=True)