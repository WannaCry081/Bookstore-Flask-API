from App.app import DB
from App.models import (
    BookModel,
    UserBookModel,
    UserModel
)
from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


BOOK_API : Blueprint = Blueprint("BOOK_API", __name__)


@BOOK_API.route("/", methods=["GET"])
def getBookList():
    book_list : list = []
    try:
        books : BookModel = BookModel.query.all()

        for book in books:
            book_list.append({
                "id" : book.id,
                "title" : book.title,
                "genre" : book.genre
            })
        
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "books" : book_list,
        "status" : 200
    }), 200


@BOOK_API.route("/<int:book_id>/<book_title>/", methods=["GET"])
def getBookDetail(book_id : int, book_title : str):
    
    try: 
        book : BookModel = BookModel.query.filter_by(
            id = book_id, title = book_title).first()

        if book:  
            return jsonify({
                "book" : book.toObject(),
                "status" : 200
            }), 200
    
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "status" : "Book does not Exists",
        "status" : 404
    }), 404


# USER ROUTES ================================================

@BOOK_API.route("/user-book-list/", methods=["GET"])
@jwt_required()
def getUserBookList():

    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:

            book_list : list = []
            
            userBooks : UserBookModel = UserBookModel.query.filter_by(
                user_id = user.id
            ).all()

            for userBook in userBooks:
                book : BookModel = BookModel.query.filter_by(id = userBook.book_id).first()
                book_list.append(book.toObject())

            return jsonify({
                "book" : book_list,
                "status" : 200
            }), 200
    
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404


@BOOK_API.route("/user-book-list/", methods=["POST"])
@jwt_required()
def addUserBook():
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()
        
        if user:

            title = request.form["title"]
            book : BookModel = BookModel.query.filter_by(title = title).first()

            if not book:
                return jsonify({
                    "message" : "Book does not Exists",
                    "status" : 404
                }), 404
            
            userBook : UserBookModel = UserBookModel(
                user_id = user.id,
                book_id = book.id
            )
            user.no_of_books = int(user.no_of_books) + 1

            DB.session.add(userBook)
            DB.session.commit()

            return jsonify({
                "message" : "Successfully Added Book", 
                "status" : 200
            }), 200
        
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404



@BOOK_API.route("/<int:book_id>/<book_title>/", methods=["DELETE"])
@jwt_required()
def deleteUserBook(book_id : int, book_title : str):
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:    

            book : BookModel = BookModel.query.filter_by(
                id = book_id,
                title = book_title
            ).first()

            userBook : UserBookModel = UserBookModel.query.filter_by(
                user_id = user.id,
                book_id = book.id
            ).first()
            
            user.no_of_books = int(user.no_of_books) - 1
            DB.session.delete(userBook)
            DB.session.commit()

            return jsonify({
                "message" : "Successfully Deleted", 
                "status" : 200
            }), 200
    except: 
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "message" : "User does not Exists",
        "status" : 404
    }), 404
