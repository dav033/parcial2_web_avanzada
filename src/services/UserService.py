from Config.db import db, ma, app
from models.User import User

class UserService:
    def create_user(self, name , role_id, email, password):
        new_user = User(name, role_id, email, password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    def search_user(self, user_id):
        return User.query.get(user_id)

    def get_users(self):
        users = User.query.all()
        return users