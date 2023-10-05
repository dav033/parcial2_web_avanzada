from Config.db import db, ma, app

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    base_remuneration = db.Column(db.Float)
    production = db.relationship('Production', backref='products', lazy=True)
    
    def __init__(self, name, base_remuneration):
        self.name = name
        self.price = base_remuneration
        
with app.app_context():
    db.create_all()
    
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'base_remuneration')
       