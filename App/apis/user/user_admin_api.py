from App.app import DB
from App.models import UserModel
from flask import (
    Blueprint,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)


USER_ADMIN_API : Blueprint = Blueprint("USER_ADMIN_API", __name__)


# ADMIN ROUTES ================================================

@USER_ADMIN_API.route("/", methods=["GET"])
@jwt_required()
def getUserAccounts():
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user.id == 1:
            user = UserModel.query.all()
            return jsonify({
                "users" : user.toObject(),
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


@USER_ADMIN_API.route("/<user_id>/<username>/<email>/", methods=["DELETE"])
@jwt_required()
def deleteAccounts(user_id : int, username : str, email : str):
    try:    
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()
        
        if user.id == 1:
            
            user : UserModel = UserModel.query.filter_by(
                id = user_id,
                username = username,
                email = email
            )

            if not user:
                return jsonify({
                    "message" : "User does not Exists",
                    "status" : 404
                }), 404
            
            DB.session.delete(user)
            DB.session.commit()
            return jsonify({
                "message" : "Successfully Deleted User",
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

