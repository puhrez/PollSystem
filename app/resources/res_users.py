from app import db
from flask.ext.restful import reqparse, Resource
from app.models import User
from sqlalchemy.exc import IntegrityError
import bcrypt
from .res_errors import not_found
userparser = reqparse.RequestParser()
userparser.add_argument('name', type=str, required=True)
userparser.add_argument('email', type=str, required=True)
userparser.add_argument('password', type=str, required=True)


class UserList(Resource):
    """
    This resource represents the collection of all users
    """

    def get(self):
        print "hit list get"
        users = User.query.all()
        return [user.as_dict() for user in users]

    def post(self):
        args = userparser.parse_args()
        user = User(
            name=args['name'],
            email=args['email'],
            password=bcrypt.hashpw(args['password'], bcrypt.gensalt(10))
        )
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError, exc:
            return {"error": exc.message}, 500
        return user.as_dict(), 201


class UserView(Resource):
    """
    This resource represents a single user
    """
    def get(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            return user.as_dict()
        else:
            return not_found("User %d" % user_id), 404

    def put(self, user_id):
        """
        TODO: don't require the entire object, only the field being changed
        """
        args = userparser.parse_args()
        user = User.query.get(user_id)
        if user is not None:
            user.name = args['name']
            user.email = args['email']
            user.password = bcrypt.hashpw(args['password'], bcrypt.gensalt(10))
            db.session.commit()
            return user.as_dict()
        else:
            return not_found("User %d" % user_id), 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return {}, 200
        else:
            return not_found("User %d" % user_id), 404
