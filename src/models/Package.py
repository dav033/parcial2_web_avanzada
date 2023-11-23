from Config.db import db, ma, app
from models.Product import Product
from models.User import User

class Packages(db.Model):
    __tablename__ = "packages"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(50))
    total_package_value = db.Column(db.Float)
    products_count = db.Column(db.Integer)
    is_complete = db.Column(db.Boolean)
    updatedAt = db.Column(db.DateTime)
    product = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def __init__(self, date, product, user_id, total_package_value, products_count,is_compleate):
        self.date = date
        self.product = product
        self.user_id = user_id
        self.total_package_value = total_package_value
        self.products_count = products_count
        self.is_complete = is_compleate

    def to_json(self):
        return {
            'id': self.id,
            'date': self.date,
            'product':self.product,
            'user_id': self.user_id,
            'total_package_value': self.total_package_value,
            'products_count': self.products_count,
            'is_complete': self.is_complete,
            'updatedAt': self.updatedAt
        }
        
with app.app_context():
    db.create_all()
    
class ProductionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'product', 'user_id', 'total_package_value', 'products_count','is_compleate', 'updatedAt')