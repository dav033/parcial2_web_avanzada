from Config.db import db, ma, app
from models.Product import Product

class ProductService:
    def get_products(self):
        products = Product.query.all()
        product_list = []
        for product in products:
            product_list.append(product.to_json())
        return product_list
    def create_product(self, name, description, value):
        new_product = Product(name, description, value)
        db.session.add(new_product)
        db.session.commit()
        return new_product
    def modify_product(self, product_id, name , description, value):
        product = Product.query.get(product_id)
        product.name = name
        product.description = description
        product.value = value
        db.session.commit()
        return product
    def getProduct(self,product_id):
        product = Product.query.get(product_id)
        return product