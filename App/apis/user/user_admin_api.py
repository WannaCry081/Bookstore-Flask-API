from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required
)


USER_ADMIN_API : Blueprint = Blueprint("USER_ADMIN_API", __name__)


# ADMIN ROUTES ================================================

@USER_ADMIN_API.route("/", methods=["GET"])
@jwt_required()
def getAccounts():
    return jsonify({})


@USER_ADMIN_API.route("/", methods=["DELETE"])
@jwt_required()
def deleteAccounts():
    return jsonify({})

