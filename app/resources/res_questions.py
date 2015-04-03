from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Question
from sqlalchemy.exc import IntegrityError


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
