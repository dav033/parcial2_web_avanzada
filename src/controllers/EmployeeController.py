from flask import request, jsonify, Blueprint
from services.EmployeeService import EmployeeService
from Security import Security

employee_service = EmployeeService()
employee_routes = Blueprint("employee_routes", __name__)


@employee_routes.route("/employee", methods=["POST"])
def create_employee():
    token_succes = Security.verify_token(request.headers)
    if (token_succes):
        data = request.get_json()
        name = data.get("name")
        roleID = data.get("roleID")
        email = data.get("email")
        password = data.get("password")
        employee_service.create_employee(name, roleID, email, password)
        return "Empleado creado", 200
    else:
        return "Unauthorized", 401
