from flask import request, jsonify, Blueprint
from services.ProductService import ProductService

product_service = ProductService()
product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/get_products", methods=["GET"])
def get_products():
    products = product_service.get_products()
    return products, 201

@product_routes.route("/create_product", methods=["POST"])
def create_product():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    value = data.get("value")
    new_product = product_service.create_product(
        name, description, value)
    return "The product has been created", 201

@product_routes.route("/modify_product", methods=["PUT"])
def modify_product():
    data = request.get_json()
    product_id = data.get("productId")
    name = data.get("name")
    description = data.get("description")
    value = data.get("value")
    product_service.modify_product(product_id,
        name, description,value)
    return "The product has been modified", 201