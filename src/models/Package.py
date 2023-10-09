from Config.db import db, ma, app
from models.Product import Product
from models.User import User

class Production(db.Model):
    __tablename__ = "packages"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(50))
    total_package_value = db.Column(db.Float)
    products_count = db.Column(db.Integer)
    product = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    
    def __init__(self, date, product, user_id, total_package_value, products_count):
        self.date = date
        self.product = product
        self.user_id = user_id
        self.total_package_value = total_package_value
        self.products_count = products_count
        
with app.app_context():
    db.create_all()
    
class ProductionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'product', 'user_id', 'total_package_value', 'products_count')