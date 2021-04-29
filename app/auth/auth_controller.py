from flask import jsonify, request
from .auth_model import users, User
from ..utils.validator import AuthValidator
from flask_jwt_extended import create_access_token, JWTManager
from app import app
import os

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ.get("SECRET_KEY")
jwt = JWTManager(app)


class UserController:

    def create_user(self):
        request_data = request.get_json()
        email = request_data['email']
        password = request_data['password']

        if not email:
            return jsonify({
                "message": "email is required",
                "status": 400
            }), 400

        if not AuthValidator.validate_user_email(email):
            return jsonify({
                "message": "Invalid email",
                "status": 400
            }), 400

        if not password:
            return jsonify({
                "message": "password is required",
                "status": 400
            }), 400

        if not AuthValidator.validate_user_password(password):
            return jsonify({
                "message": "password should be longer than 8 characters",
                "status": 400
            }), 400

        user = User(email=email, password=password).to_dict()
        users.append(user)
        return jsonify({"user": user}), 201

    def login_user(self):
        request_data = request.get_json()
        email = request_data['email']
        password = request_data['password']

        for user in users:
            if user["password"] == password and user["email"] == email:
                token = create_access_token(identity=email)
                return jsonify({
                    "message": "Login successful",
                    "status": 200,
                    "token": token
                }), 200
        return jsonify({
            "message": "User with credentials doesnot exist",
            "status": 404,
        }), 404
