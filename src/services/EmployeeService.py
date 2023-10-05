from Config.db import db, ma, app
from models.Employee import Employee

class EmployeeService:
    def create_employee(self, name , role):
        new_user = Employee(name, role)
        db.session.add(new_user)
        db.session.commit()
        return new_user