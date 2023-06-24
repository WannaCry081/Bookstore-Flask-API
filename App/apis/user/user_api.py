from App.app import DB, BCRYPT
from App.models import UserModel, UserBookModel
from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    unset_jwt_cookies,
    unset_access_cookies
)


USER_API : Blueprint = Blueprint("USER_API", __name__)


# USER ROUTES ================================================

@USER_API.route("/", methods=["GET"])
@jwt_required()
def getProfile():
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:
            return jsonify({
                "user" : user.toObject(),
                "status" : 200
            }), 200
        
    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500

    return jsonify({
        "status" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/", methods=["PUT"])
@jwt_required()
def updateProfile():    
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:
            data = request.get_json()
            username = data["username"]
            bio = data["bio"]

            
            if username:
                if len(username) < 4:
                    return jsonify({
                        "message" : "Invalid Username", 
                        "status" : 400
                    }), 400
                
                user.username = username
                    
            user.bio = bio
            DB.session.commit()
            return jsonify({
                "message" : "Successfully Updated Profile",
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


@USER_API.route("/", methods=["POST"])
@jwt_required()
def updatePassword():
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:
            old_password = request.form["old_password"]
            new_password = request.form["new_password"]

            if BCRYPT.check_password_hash(user.password, old_password):
                
                if len(new_password) < 6:
                    return jsonify({
                        "message" : "Password must be at least 6 characters long", 
                        "status" : 400
                    }), 400
            
                user.password = BCRYPT.generate_password_hash(new_password)
                DB.session.commit()
                return jsonify({
                    "message" : "Successfully Updated Password",
                    "status" : 200
                }), 200
        
            else:
                return jsonify({
                    "message" : "Incorrect Password",
                    "status" : 400
                }), 400

    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500

    return jsonify({
        "status" : "User does not Exists",
        "status" : 404
    }), 404


@USER_API.route("/", methods=["DELETE"])
@jwt_required()
def deleteProfile(): 
    try:
        access_token = get_jwt_identity()
        user : UserModel = UserModel.query.filter_by(email = access_token).first()

        if user:
            response = jsonify({
                "message" : "Successfully Deleted",
                "status" : 200
            })

            userBooks : UserBookModel = UserBookModel.query.filter_by(
                user_id = user.id
            ).all()

            if userBooks:
                for userBook in userBooks:
                    DB.session.delete(userBook)

            DB.session.delete(user)
            DB.session.commit()

            unset_access_cookies(response)
            unset_jwt_cookies(response)

            return response, 200

    except:
        return jsonify({
            "message" : "Internal Server Error",
            "status" : 500
        }), 500

    return jsonify({
        "status" : "User does not Exists",
        "status" : 404
    }), 404

