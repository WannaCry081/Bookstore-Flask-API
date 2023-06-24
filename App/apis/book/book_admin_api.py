from App.app import DB
from App.models import (
    UserModel,
    BookModel,
    UserBookModel
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


BOOK_ADMIN_API : Blueprint = Blueprint("BOOK_ADMIN_API", __name__)


# ADMIN ROUTES ================================================

@BOOK_ADMIN_API.route("/", methods=["POST"])
@jwt_required()
def createBook():
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        # Not Secured, Must Change Condition
        if user.id == 1:
            title = request.form["title"]
            author = request.form["author"]
            genre = request.form["genre"]
            description = request.form["description"]
            price = request.form["price"]

            if not title:
                return jsonify({
                    "message" : "Title property must not be Empty",
                    "status" : 400        
                }), 400
            
            if not author:
                return jsonify({
                    "message" : "Author property must not be Empty",
                    "status" : 400        
                }), 400
            
            if not genre:
                return jsonify({
                    "message" : "Genre property must not be Empty",
                    "status" : 400        
                }), 400
            
            book : BookModel = BookModel.query.filter_by(title = title).first()
            if book:
                return jsonify({
                    "message" : "Book already exists",
                    "status" : 400
                }), 400
            
            book = BookModel(
                title = title,
                author = author,
                genre = genre,
                description = description,
                price = price
            )

            DB.session.add(book)
            DB.session.commit()

            return jsonify({
                "message" : "Successfully Created",
                "status" : 200
            }), 200
            
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "status" : "Page does not Exists",
        "status" : 404
    }), 404


@BOOK_ADMIN_API.route("/<int:book_id>/<book_title>/", methods=["PUT"])
@jwt_required()
def updateBookDetail(book_id : int, book_title : str):
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user.id == 1:    
            data = request.get_json()
            description = data["description"]
            price = data["price"]

            book : BookModel = BookModel.query.filter_by(
                id = book_id,
                title = book_title
            ).first()

            if not book:
                return jsonify({
                    "message" : "Book does not Exists",
                    "status" : 404
                }), 404
            
            if description:
                book.description = description

            if price:
                book.price = price 
            DB.session.commit()

            return jsonify({
                "message" : "Successfully Updated",
                "status" : 200
            }), 200

    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500
    
    return jsonify({
        "status" : "Page does not Exists",
        "status" : 404
    }), 404


@BOOK_ADMIN_API.route("/<int:book_id>/<book_title>/", methods=["DELETE"])
@jwt_required()
def deleteBook(book_id : int, book_title : str):
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()
        
        # Not Secured, Must Change Condition
        if user.id == 1:
            book : BookModel = BookModel.query.filter_by(
                id = book_id, 
                title = book_title
            ).first()

            if not book:
                return jsonify({
                    "message" : "Book does not Exists", 
                    "status" : 404
                }), 404

            userBooks : UserBookModel = UserBookModel.query.filter_by(
                book_id = book_id
            ).all()

            if userBooks:
                for userBook in userBooks:
                    DB.session.delete(userBook)
                    
            DB.session.delete(book)
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
        "status" : "Page does not Exists",
        "status" : 404
    }), 404