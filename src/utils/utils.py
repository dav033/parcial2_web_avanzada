from models.Product import Product
from models.User import User
from services.UserService import UserService
from services.RoleService import RoleService
from models.Role import Role
from services.ProductService import ProductService

user_service = UserService()
role_service = RoleService()
product_service = ProductService()

def getTotalPackagevalue(productid:Product,user_id):
        user:User = user_service.search_user(user_id)
        role:Role = role_service.getRole(user.roleID)
        
        roleBonus:Role = role.compensationPerProduct
        product:Product = product_service.getProduct(productid)

        totalPackageValue = (product.value * roleBonus)*12

        return totalPackageValue;