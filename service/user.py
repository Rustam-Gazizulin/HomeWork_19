import base64
import hashlib

from dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATION


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATION
        ))
