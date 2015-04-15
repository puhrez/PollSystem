from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Token, Poll
from sqlalchemy.exc import IntegrityError
from .res_errors import not_found
tokenparser = reqparse.RequestParser()
tokenparser.add_argument('value', type=int, required=True)
tokenparser.add_argument('maximum', type=int, required=True)
tokenparser.add_argument('minimum', type=int, required=True)
tokenparser.add_argument('poll_id', type=int, required=True)
tokenparser.add_argument('name', type=str, required=True)


class TokenList(Resource):
    """
    This resource represents the collection of Tokens
    """
    def get(self):
        tokens = Token.query.all()
        return [token.as_dict() for token in tokens]


class TokenPollList(Resource):
    """
    This resource represents the collection of Tokens for a specific Poll
    """
    def get(self, poll_id):
        poll = Poll.query.get(poll_id)
        if poll is not None:
            tokens = poll.tokens.all()
            return [token.as_dict() for token in tokens]
        else:
            return not_found("Poll %d" % poll_id), 404

    def post(self, poll_id):
        args = tokenparser.parse_args()
        token = Token(
            name=args['name'],
            poll_id=args['poll_id'],
            maximum=args['maximum'],
            minimum=args['minimum'],
            value=args['value']
        )
        try:
            db.session.add(token)
            db.session.commit()
        except IntegrityError, exc:
            return {"error": exc.message}, 500
        return token.as_dict(), 201


class TokenView(Resource):
    """
    This resource represents a single Token
    """
    def get(self, token_id):
        token = Token.query.get(token_id)
        if token is not None:
            return token.as_dict()
        else:
            return not_found("Token %d" % token_id), 404

    def put(self, token_id):
        args = tokenparser.parse_args()
        token = Token.query.get(token_id)
        if token is not None:
            token.name = args['name']
            token.value = args['value']
            token.maximum = args['maximum']
            token.minimum = args['minimum']
            token.poll_id = args['poll_id']
            db.session.commit()
            return token.as_dict, 200
        else:
            return not_found("Token %d" % token_id), 404

    def delete(self, token_id):
        token = Token.query.get(token_id)
        if token is not None:
            db.session.delete(token)
            db.session.commit()
            return {}, 200
        else:
            return not_found("Token %d" % token_id), 404
