from Config.db import db, ma, app


class Employee(db.Model):
    __tablename__ = "employees"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(50))
    production = db.relationship('Production', backref='employee', lazy=True)
    
    
    def __init__(self, name, role):
        self.name = name
        self.role = role

with app.app_context():
    db.create_all()

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'role')
