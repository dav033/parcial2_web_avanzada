from Config.db import db, ma, app

class Role(db.Model):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    CompensationPerProduct = db.Column(db.Float)
    user = db.relationship('User', backref='roles', lazy=True)
    
    def __init__(self, name , role):
        self.name = name
        self.role = role
        
        
with app.app_context():
    db.create_all()
    
class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'CompensationPerProduct')