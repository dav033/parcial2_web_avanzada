from flask import request, jsonify, Blueprint
from Security import Security
from services.PackageService import PackageService

package_routes = Blueprint("package_routes", __name__)

package_service = PackageService()


@package_routes.route("/create_or_update_package", methods=["POST"])
def create_or_update_package():
        data = request.get_json()
        user_id = data.get("user_id")
        count = data.get("count")
        package_product_type = data.get("product_type")
        print(user_id , count , package_product_type)
        try:
            packageExist = package_service.getPackage(user_id,package_product_type)
            if packageExist:
                package_service.UpdatePackage(packageExist,count)
                return jsonify({
                    "Stauts": 200,
                    }),200
            package_service.createPackage(user_id, package_product_type,count)

            return jsonify({
                "Stauts": 201,
                "Message": "Package Created"
            })
        except Exception as error:
            print(error)
            return jsonify({"Status": 500, "Error": str(error)}), 500

@package_routes.route("/get_packages", methods=["GET"])
def get_packages():
    try:
        packages = package_service.getPackages()
        return {"packages": list(map(lambda package: package.to_json(), packages))}, 200
    except Exception as error:
        print(error)
        return jsonify({"Status": 500, "Error": str(error)}), 500