from Config.db import db, ma, app
from models.Product import Product
from models.Employee import Employee

class Production(db.Model):
    __tablename__ = "productions"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(50))
    time = db.Column(db.String(50))
    product = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    
    def __init__(self, date, time, product, user_id):
        self.date = date
        self.time = time
        self.product = product
        self.user_id = user_id
        
with app.app_context():
    db.create_all()
    
class ProductionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'time', 'product')