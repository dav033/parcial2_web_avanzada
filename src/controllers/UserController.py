from flask import request, jsonify, Blueprint
from services.UserService import UserService

user_service = UserService()
user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/create_user", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    role = data.get("role")
    email = data.get("email")
    password = data.get("password")
    new_user = user_service.create_user(
        name, role, email, password)
    return "The user has been created", 201

@user_routes.route("/search_user", methods=["GET"])
def search_user():
    user_id = request.args.get('user_id')
    user = user_service.search_user(user_id)
    return user.to_json(), 200 

