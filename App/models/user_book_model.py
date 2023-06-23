from App.app import DB


class UserBookModel(DB.Model):
    __tablename__ = "user_books"

    id = DB.Column(DB.Integer, primary_key = True)

    user_id = DB.Column(DB.Integer, DB.ForeignKey("users.id"))
    book_id = DB.Column(DB.Integer, DB.ForeignKey("books.id"))


    def __repr__(self) -> str:
        return "<UserBooks %r>"%self.id
