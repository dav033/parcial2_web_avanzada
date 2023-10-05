from flask import request, jsonify, Blueprint
from services.EmployeeService import EmployeeService

employee_service = EmployeeService()
employee_routes = Blueprint("employee_routes", __name__)

@employee_routes.route("/employee", methods=["POST"])
def create_employee():
    data = request.get_json()
    name = data.get("name")
    role = data.get("role")
    new_employee = employee_service.create_employee(name, role)
    return "Usuario Creado", 201 
