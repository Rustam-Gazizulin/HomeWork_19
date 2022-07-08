from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service


genre_ns = Namespace('user')


@genre_ns.route('/')
class UserView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200