from app import db
from flask.ext.restful import reqparse, Resource
from app.models import User
from sql.alchemy.exc import IntegrityError
userparser = reqparse.RequestParser()
userparser.add_arguement('name', type=str, required=True)
userparser.add_arguement('email', type=str, required=True)
userparser.add_arguement('password', type=str, required=True)


class UserList(Resource):
    """
    This resource represents the collection of all users
    """
    error_msg = {
        "404":
        {"error": "User not found"}
    }

    def get(self):
        users = User.query.all()
        if users is not None:
            return users.as_dict()
        else:
            return {}, 404

    def post(self):
        args = userparser.parse_args()
        user = User(
            name=args['name'],
            email=args['email'],
            password=args['password']
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError, exc:
            return {"error": exc.message}, 500

        return user.as_dict, 201


class UserView(Resource):
    """
    This resource represents a single user
    """
    def get(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            return user.as_dict()
        else:
            return self.error_msg['404'], 404

    def put(self, user_id):
        """
        TODO: don't require the entire object, only the field being changed
        """
        args = userparser.parse_args()
        user = User.query.get(user_id)
        self.abort()
        if user is not None:
            user = User(
                name=args['name'],
                email=args['email'],
                password=args['password']
            )
            db.session.commit()
            return user, 200
        else:
            return self.error_msg['404'], 404

    def delete(self, user_id):
        user = User.query.get(user_id)
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return {}, 200
        else:
            return self.error_msg['404'], 404
