from flask import Flask, request, jsonify, redirect, render_template
from controllers.EmployeeController import employee_routes
from controllers.ProductionController import production_routes
from controllers.AuthController import auth_routes
from Config.db import db, ma, app
# app.register_blueprint(ruta_cliente, url_prefix = "/api" )
# app.register_blueprint(ruta_prestamo, url_prefix = "/api" )

app.register_blueprint(auth_routes, url_prefix = "/api/auth" )
app.register_blueprint(employee_routes, url_prefix = "/api" )
app.register_blueprint(production_routes, url_prefix = "/api")
@app.route("/ ")
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')