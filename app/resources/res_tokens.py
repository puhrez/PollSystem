from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Token
from sqlalchemy.exc import IntegrityError
tokenparser = reqparse.RequestParser()
tokenparser.add_argument('value', type=int, required=True)
tokenparser.add_argument('maximum', type=int, required=True)
tokenparser.add_argument('minimum', type=int, required=True)
tokenparser.add_argument('poll_id', type=int, required=True)
tokenparser.add_argument('text', type=str, required=True)


class TokenPollList(Resource):
    """
    This resource represents the collection of Tokens for a specific Poll
    """
    def get(self, poll_id):
        pass

    def post(self, poll_id):
        pass


class TokenList(Resource):
    """
    This resource represents the collection of Tokens
    """
    def get(self):
        pass

    def post(self):
        pass


class TokenView(Resource):
    """
    This resource represents a single Token
    """
    def get(self, token_id):
        pass

    def put(self, token_id):
        pass

    def delete(self, token_id):
        pass
