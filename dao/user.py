from dao.model.user import User


class UserDao:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        pass

    def delete(self, uid):
        pass

    def update(self, user_data):
        pass