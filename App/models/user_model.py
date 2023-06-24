from App.app import DB


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