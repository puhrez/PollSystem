from app import db
from flask.ext.restful import reqparse, Resource
from app.models import Question, Poll
from sqlalchemy.exc import IntegrityError
questionparser = reqparse.RequestParser()
questionparser.add_argument('text', type=str, required=True)
questionparser.add_argument('poll_id', type=int, required=True)


class QuestionList(Resource):
    error_msg = {
        "poll": {
            "404":
            {"error": "Poll not found"}
        },
        "question": {
            "404":
            {"error": "Question not found"}
        }
    }
    """
    This resource represents the collection of Questions
    """
    def get(self):
        questions = Question.query.all()
        results = []
        for question in questions:
            results.append(question.as_dict())
        return results


class QuestionPollList(Resource):
    """
    This resource represents the collection of Questions for a specific Poll
    """
    def get(self, poll_id):
        poll = Poll.query.get(poll_id)
        if poll is not None:
            questions = poll.questions.all()
            results = []
            for question in questions:
                results.append(question.as_dict())
            print 'from specific list view', results
            return results
        else:
            return self.error_msg["poll"]["404"], 404

    def post(self, poll_id):
        args = questionparser.parse_args()
        question = Question(
            text=args['text'],
            poll_id=args['poll_id']
        )
        try:
            db.session.add(question)
            db.session.commit()
        except IntegrityError, exc:
            return {"error": exc.message}, 500
        return question.as_dict(), 201


class QuestionView(Resource):
    """
    This resource represents a single Question
    """
    def get(self, question_id):
        question = Question.query.get(question_id)
        if question is not None:
            return question.as_dict()
        else:
            return self.error_msg["question"]["404"], 404

    def put(self, question_id):
        args = questionparser.parse_args()
        question = Question.query.get(question_id)
        if question is not None:
            question.text = args['text']
            question.poll_id = args['poll_id']
            db.session.commit()
            return question.as_dict(), 404
        else:
            return self.error_msg["question"]["404"], 404

    def delete(self, question_id):
        question = Question.query.get(question_id)
        if question is not None:
            db.session.delete(question)
            db.session.commit()
            return {}, 200
        else:
            return self.error_msg['question']['404'], 404
