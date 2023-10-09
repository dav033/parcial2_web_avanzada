from Config.db import db, ma, app
from models.Role import Role


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    roleID = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)

    def __init__(self, name, roleID, email, password):
        self.name = name
        self.roleID = roleID
        self.email = email
        self.password = password
        
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'roleID': self.roleID
        }

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "roleID": self.roleID
        }


with app.app_context():
    db.create_all()


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "roleID", "email", "password")
