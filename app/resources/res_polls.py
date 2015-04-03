from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Poll
from sqlalchemy.exc import IntegrityError


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