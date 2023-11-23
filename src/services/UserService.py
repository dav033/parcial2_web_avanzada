from Config.db import db, ma, app
from models.User import User
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    def create_user(self, name , role_id, email, password):
        hashed_password = generate_password_hash(password)
        new_user = User(name, role_id, email, hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    def search_user(self, user_id):
        return User.query.get(user_id)

    def get_users(self):
        users = User.query.all()
        return users
    def delete_user(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return user