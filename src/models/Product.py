from Config.db import db, ma, app

class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    value = db.Column(db.Float)
    
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description':self.description,
            'value': self.value,
        }
        
with app.app_context():
    db.create_all()
    
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'value')
       