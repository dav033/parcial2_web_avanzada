from flask import Flask, request, jsonify, redirect, render_template
from controllers.UserController import user_routes
from controllers.RoleController import role_routes
from controllers.ProductController import product_routes
from controllers.AuthController import auth_routes
from controllers.PackageController import package_routes
from Config.db import db, ma, app

app.register_blueprint(auth_routes, url_prefix = "/api" )
app.register_blueprint(user_routes, url_prefix = "/api" )
app.register_blueprint(role_routes, url_prefix = "/api")
app.register_blueprint(product_routes, url_prefix = "/api")
app.register_blueprint(package_routes, url_prefix = "/api")

@app.route("/")
def index():
    return "Welcome to API Web"

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0')