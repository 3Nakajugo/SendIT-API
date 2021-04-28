from flask import jsonify, request
from .auth_model import users, User
from ..utils.validator import AuthValidator


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
        return jsonify(user), 201
