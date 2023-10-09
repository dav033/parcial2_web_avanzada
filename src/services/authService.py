from flask import request, jsonify
from models.User import Employee
from Security import Security


class AuthService():
    def login_user(cls, name, password):

        user = Employee.query.filter_by(name=name).first()

        if (user and user.password == password):
            token = Security.generate_token(user)
            return jsonify({"token": token, "user": user.to_json()})
        else:
            return False
