from .extensions import db
from flask_login import UserMixin

class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.string(100))
    name = db.Column(db.String(100))
    lists = None