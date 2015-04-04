from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Effect, Question
from sqlalchemy.exc import IntegrityError
from .res_errors import not_found
effectparser = reqparse.RequestParser()
effectparser.add_argument('value', type=int, required=True)
effectparser.add_argument('question_id', type=int, required=True)
effectparser.add_argument('token_id', type=int, required=True)


class EffectList(Resource):
    """
    This resource represents the collection of effects
    """
    def get(self):
        effects = Effect.query.all()
        results = []
        for effect in effects:
            results.append(effect.as_dict())
        return results


class EffectQuestionList(Resource):
    """
    This resource represents a collection of effects for a specific question
    """
    def get(self, question_id):
        question = Question.query.get(question_id)
        if question is not None:
            effects = question.effects.all()
            results = []
            for effect in effects:
                results.append(question.as_dict())
            return results
        else:
            return not_found("Question %d" % question_id), 404

    def post(self, question_id):
        args = effectparser.parse_args()
        effect = Effect(
            value=args['value'],
            question_id=args['question_id'],
            token_id=args['token_id']
        )
        try:
            db.session.add(effect)
            db.session.commit()
        except IntegrityError, exc:
            return {"error": exc.message}, 500
        return effect.as_dict(), 201


class EffectView(Resource):
    """
    This resource represents a specifc effects
    """
    def get(self, effect_id):
        effect = Effect.query.get(effect_id)
        if effect is not None:
            return effect.as_dict()
        else:
            return not_found("Effect %d" % effect_id), 404

    def put(self, effect_id):
        args = effectparser.parse_args()
        effect = Effect.query.get(effect_id)
        if effect is not None:
            effect.value = args['value']
            effect.question_id = args['question_id']
            effect.token_id = args['token_id']
            db.session.commit()
            return effect.as_dict(), 200
        else:
            return not_found("Effect %d" % effect_id), 404

    def delete(self, effect_id):
        pass
