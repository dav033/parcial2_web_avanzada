from flask import request, jsonify, Blueprint
from services.ProductService import ProductService
from Security import Security

product_service = ProductService()
product_routes = Blueprint("product_routes", __name__)


@product_routes.route("/get_products", methods=["GET"])
def get_products():
    token_succes = Security.verify_token(request.headers)
    if (token_succes):
        products = product_service.get_products()
        return jsonify(products), 200
    else:
        return "Invalid Token", 401


@product_routes.route("/create_product", methods=["POST"])
def create_product():
    token_succes = Security.verify_token(request.headers)
    if (token_succes):
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        value = data.get("value")
        new_product = product_service.create_product(
            name, description, value)
        return "The product has been created", 201
    else:
        return "Invalid Token", 401


@product_routes.route("/modify_product", methods=["PUT"])
def modify_product():
    token_succes = Security.verify_token(request.headers)
    if (token_succes):
        data = request.get_json()
        product_id = data.get("product_id")
        name = data.get("name")
        description = data.get("description")
        value = data.get("value")
        product = product_service.modify_product(
            product_id, name, description, value)
        return product.to_json(), 200
    else:
        return "Invalid Token", 401
