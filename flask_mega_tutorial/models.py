from flask_login import UserMixin

from flask_mega_tutorial import bcrypt, db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(40), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False, unique=False)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
