from flask import request, jsonify, Blueprint
from services.ProductionService import ProductionService

production_service = ProductionService()
production_routes = Blueprint("production_routes", __name__)

@production_routes.route("/production", methods=["POST"])
def create_production():
    data = request.get_json()
    user_id = data.get("user_id")
    new_production = production_service.create_production(user_id)
    return "Produccion Creada", 201