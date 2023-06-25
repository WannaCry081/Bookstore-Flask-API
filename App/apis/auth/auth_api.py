from App.models import UserModel
from App.app import BCRYPT, DB
from App.utils.validity import isValidEmail
from flask import (
    Blueprint,
    request,
    jsonify
)
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
)


AUTH_API: Blueprint = Blueprint("AUTH_API", __name__)


@AUTH_API.route("/signup/", methods=["POST"])
def signUpUser():
    try:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        user: UserModel = UserModel.query.filter_by(
            username=username,
            email=email
        ).first()

        if not user:
            if username is None or len(username) < 4:
                return jsonify({
                    "auth": False,
                    "message": "Username must be at least 4 characters long",
                    "status": 400
                }), 400

            if not isValidEmail(email):
                return jsonify({
                    "auth": False,
                    "message": "Invalid Email Address",
                    "status": 400
                }), 400

            if len(password) < 6:
                return jsonify({
                    "auth": False,
                    "message": "Password must be at least 6 characters long",
                    "status": 400
                }), 400

            user = UserModel(
                username=username,
                email=email,
                password=BCRYPT.generate_password_hash(password)
            )

            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            response = jsonify({
                "auth": True,
                "access_token": access_token,
                "message": "Access Authorized",
                "status": 200
            })

            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            DB.session.add(user)
            DB.session.commit()

            return response, 200

    except:
        return jsonify({
            "auth": False,
            "message": "Internal Server Error",
            "status": 500
        }), 500

    return jsonify({
        "auth": False,
        "message": "User already exists",
        "status": 400,
    }), 400


@AUTH_API.route("/signin/", methods=["POST"])
def signInUser():
    try:
        email = request.form["email"]
        password = request.form["password"]

        user: UserModel = UserModel.query.filter_by(email=email).first()

        if user:
            if BCRYPT.check_password_hash(user.password, password):
                access_token = create_access_token(identity=email)
                refresh_token = create_refresh_token(identity=email)
                response = jsonify({
                    "auth": True,
                    "access_token": access_token,
                    "message": "Authorized Access",
                    "status": 200,
                })

                set_access_cookies(response, access_token)
                set_refresh_cookies(response, refresh_token)
                return response, 200

            else:
                return jsonify({
                    "auth": False,
                    "message": "Incorrect Password",
                    "status": 400
                }), 400

    except:
        return jsonify({
            "auth": False,
            "message": "Internal Server Error",
            "status": 500
        }), 500

    return jsonify({
        "auth": False,
        "message": "User does not exist",
        "status": 404,
    }), 404


@AUTH_API.route("/signout/", methods=["POST"])
def signOutUser():
    response = jsonify({
        "message": "Successfully Logged Out",
        "status": 200
    })
    unset_jwt_cookies(response)
    return response, 200


@AUTH_API.route("/refresh/", methods=["POST"])
@jwt_required(refresh=True)
def refreshAccessToken():
    try:
        email = get_jwt_identity()
        user: UserModel = UserModel.query.filter_by(email=email).first()

        if user:
            new_access_token = create_access_token(identity=email)
            response = jsonify({
                "access_token": new_access_token,
                "message": "Access Token Refreshed",
                "status": 200
            })
            set_access_cookies(response, new_access_token)
            return response, 200

    except:
        return jsonify({
            "message": "Internal Server Error",
            "status": 500
        }), 500

    return jsonify({
        "message": "User not found",
        "status": 404
    }), 404
