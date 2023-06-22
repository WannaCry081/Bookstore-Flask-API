from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required
)


USER_API : Blueprint = Blueprint("USER_API", __name__)


# USER ROUTES ================================================

@USER_API.route("/", methods=["GET"])
@jwt_required()
def getAccount():
    return jsonify({})


@USER_API.route("/", methods=["PUT"])
@jwt_required()
def updateAccountProfile():
    return jsonify({})


@USER_API.route("/", methods=["PUT"])
@jwt_required()
def updateAccountPassword():
    return jsonify({})


@USER_API.route("/", methods=["DELETE"])
@jwt_required()
def deleteAccount(): 
    return jsonify({})

