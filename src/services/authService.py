from flask import request, jsonify
from models.User import User
from Security import Security
from werkzeug.security import generate_password_hash, check_password_hash


class AuthService():
    def login_user(cls, name, password):
        user = User.query.filter_by(name=name).first()
        if (user and check_password_hash(user.password, password)):
            token = Security.generate_token(user)
            return jsonify({"token": token, "user": user.to_json()})
        else:
            return False
