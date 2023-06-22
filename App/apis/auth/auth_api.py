from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    unset_jwt_cookies,
    unset_access_cookies,
    set_access_cookies,
    get_jwt_identity
)


AUTH_API : Blueprint = Blueprint("AUTH_API", __name__)


@AUTH_API.route("/signup/")
def signUpUser():
    return jsonify({})


@AUTH_API.route("/signin/")
def signInUser():
    return jsonify({})


@AUTH_API.route("/signout/")
@jwt_required()
def signOutUser():
    return jsonify({})