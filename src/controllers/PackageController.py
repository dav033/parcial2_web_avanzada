from flask import request, jsonify, Blueprint
from Security import Security
from services.PackageService import PackageService

package_routes = Blueprint("package_routes", __name__)

package_service = PackageService()


@package_routes.route("/create_or_update_package", methods=["POST"])
def create_or_update_package():
    token_succes = Security.verify_token(request.headers)
    if (token_succes):
        data = request.get_json()
        user_id = data.get("user_id")
        package_product_type = data.get("product_type")
        try:
            packageExist = package_service.getPackage(user_id,package_product_type)
            if packageExist:
                package = package_service.UpdatePackage(packageExist)
                return jsonify({
                    "Stauts": 200,
                    "Message": package.to_json()
                })
            package_service.createPackage(user_id, package_product_type)
            return jsonify({
                "Stauts": 201,
                "Message": "Package Created"
            })

        except Exception as error:
            return jsonify({"Status": 500, "Error": str(error)}), 500
    else:
        return "Invalid Token", 401
