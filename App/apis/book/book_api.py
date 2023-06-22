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


# USER ROUTES ================================================

@BOOK_API.route("/", methods=["GET"])
@jwt_required()
def getBooks():
    return jsonify({})


@BOOK_API.route("/<int:book_id>/<book_title>/", methods=["GET"])
@jwt_required()
def getBookDetail(book_id : int, book_title : str):
    return jsonify({})


@BOOK_API.route("/<int:book_id>/<book_title>/", methods=["POST"])
@jwt_required()
def addUserBook():
    return jsonify({})

@BOOK_API.route("/<int:book_id>/<book_title>/", methods=["DELETE"])
@jwt_required()
def deleteUserBook():
    return jsonify({})
