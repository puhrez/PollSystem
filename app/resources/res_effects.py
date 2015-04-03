from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Effect
from sqlalchemy.exc import IntegrityError


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