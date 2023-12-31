from flask import request, jsonify, Blueprint
from services.RoleService import RoleService
from Security import Security

role_service = RoleService()
role_routes = Blueprint("role_routes", __name__)


@role_routes.route("/get_roles", methods=["GET"])
def get_roles():

    roles = role_service.get_roles()
    return jsonify(roles), 200


@role_routes.route("/create_role", methods=["POST"])
def create_role():
    data = request.get_json()
    name = data.get("name")
    compensation_per_product = data.get("compensationPerProduct")
    new_role = role_service.create_role(
        name, compensation_per_product)
    return "The role has been created", 201


@role_routes.route("/modify_role", methods=["POST"])
def modify_role():
    data = request.get_json()
    role_id = data.get("rolId")
    name = data.get("name")
    compensation_per_product = data.get("compensationPerProduct")
    modified_role = role_service.modify_role(role_id,
                                             name, compensation_per_product)
    if modified_role != None:
        return "The role has been modified", 200
