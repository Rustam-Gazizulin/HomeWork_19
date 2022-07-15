from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    """Модель описывающая usera в базе данных с необходимыми полями"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)  # ставим уникальное имя чтобы корректно идентифицировать пользователя
    password = db.Column(db.String)
    role = db.Column(db.String)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()

