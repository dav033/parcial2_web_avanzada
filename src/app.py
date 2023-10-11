from flask import Flask, request, jsonify, redirect, render_template
from controllers.UserController import user_routes
from controllers.RoleController import role_routes
from controllers.ProductController import product_routes
from controllers.AuthController import auth_routes
from controllers.PackageController import package_routes
from Config.db import db, ma, app
from Security import Security

app.register_blueprint(auth_routes, url_prefix="/api")
app.register_blueprint(user_routes, url_prefix="/api")
app.register_blueprint(role_routes, url_prefix="/api")
app.register_blueprint(product_routes, url_prefix="/api")
app.register_blueprint(package_routes, url_prefix="/api")


@app.route("/")
def index():
    return "Welcome to API Web"


@app.before_request
def token_middleware():

    current_route = request.path

    excluded_routes = ["/api/login"]
    no_admin_routes = ["/api/create_or_update_package"]
    token = request.headers.get("Authorization")

    if token == None and current_route not in excluded_routes:
        return "Unauthorized", 401
    else:
        token_data = Security.verify_token(request.headers)

        if not token_data['token_valid'] and current_route not in excluded_routes:
            return "Invalid Token", 401

        if current_route not in no_admin_routes and token_data['role'] != "4":

            return "Admin required", 401


if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')
