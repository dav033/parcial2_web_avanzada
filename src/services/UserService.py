from Config.db import db, ma, app
from models.User import Employee

class EmployeeService:
    def create_employee(self, name , roleID, email, password):
        new_user = Employee(name, roleID, email, password)
        db.session.add(new_user)
        db.session.commit()
        return new_user