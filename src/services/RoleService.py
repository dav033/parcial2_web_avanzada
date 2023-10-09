from Config.db import db, ma, app
from models.Role import Role

class RoleService:
    def get_roles(self):
        roles = Role.query.all()
        role_list = []
        for role in roles:
            role_list.append(role.to_json())
        return role_list
    def create_role(self, name, compensation_per_product):
        new_role = Role(name, compensation_per_product)
        db.session.add(new_role)
        db.session.commit()
        return new_role
    def modify_role(self, role_id, name , compensation_per_product):
        role = Role.query.get(role_id)
        if role.name != "Admin":
            role.name = name
            role.compensationPerProduct = compensation_per_product
            db.session.commit()
            return role
        else:
            return None