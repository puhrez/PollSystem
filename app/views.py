from app import db, api, app
from flask.ext.restful import reqparse, abort, Resource
from .models import User, Poll, Token, Question, Effect


class UserList(Resource):
    """
    This resource represents the collection of all users
    """
    def get(self):
        pass

    def post(self):
        pass


class UserView(Resource):
    """
    This resource represents a single user
    """
    def get(self, user_id):
        pass

    def put(self, user_id):
        pass

    def delete(self, user_id):
        pass


class PollList(Resource):
    """
    This resource represents the collection of all Polls
    """
    def get(self):
        pass

    def post(self):
        pass


class PollView(Resource):
    """
    This resource represents a single Poll
    """
    def get(self, poll_id):
        pass

    def put(self, poll_id):
        pass

    def delete(self, poll_id):
        pass


class QuestionPollList(Resource):
    """
    This resource represents the collection of Questions for a specific Poll
    """
    def get(self, poll_id):
        pass

    def post(self, poll_id):
        pass


class QuestionList(Resource):
    """
    This resource represents the collection of Questions
    """
    def get(self):
        pass

    def post(self):
        pass


class QuestionView(Resource):
    """
    This resource represents a single Question
    """
    def get(self, question_id):
        pass

    def put(self, question_id):
        pass

    def delete(self, question_id):
        pass


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


class EffectQuestionList(Resource):
    """
    This resource represents a collection of effects for a specific question
    """
    def get(self, question_id):
        pass

    def post(self, question_id):
        pass


class EffectList(Resource):
    """
    This resource represents the collection of effects
    """
    def get(self):
        pass

    def post(self):
        pass


class EffectView(Resource):
    """
    This resource represents a specifc effects
    """
    def get(self, effect_id):
        pass

    def put(self, effect_id):
        pass

    def delete(self, effect_id):
        pass
"""
View endpoints
"""
api.add_resource(QuestionView, '/api/questions/<string:question_id>')
api.add_resource(TokenView, '/api/tokens/<string:token_id>')
api.add_resource(PollView, '/api/polls/<string:poll_id>')
api.add_resource(EffectView, '/api/effects/<string:effect_id>')
api.add_resource(UserView, '/api/users/<string:user_id>')

"""
collection endpoints
"""
api.add_resource(QuestionList, '/api/questions')
api.add_resource(TokenList, '/api/tokens')
api.add_resource(PollList, '/api/polls')
api.add_resource(EffectList, '/api/effects')
api.add_resource(UserList, '/api/users')
api
"""
specific collection endpoints
"""
api.add_resource(
    TokenPollList,
    '/api/polls/<string:poll_id>/<string:question_id>')
api.add_resource(
    QuestionPollList,
    '/api/polls/<string:poll_id>/<string:token_id>')
api.add_resource(
    EffectQuestionList,
    '/api/polls/<string:poll_id>/<string:token_id>')
