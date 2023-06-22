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

@BOOK_ADMIN_API.route("/")
@jwt_required()
def createBook():
    return jsonify({})


@BOOK_ADMIN_API.route("/<int:book_id>/<book_title>/")
@jwt_required()
def updateBookDetail(book_id : int, book_title : str):
    return jsonify({})


@BOOK_ADMIN_API.route("/<int:book_id>/<book_title>/")
@jwt_required()
def deleteBook(book_id : int, book_title : str):
    return jsonify({})