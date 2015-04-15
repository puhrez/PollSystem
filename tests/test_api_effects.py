import json
from nose.tools import eq_
from app.models import Question, Effect, Poll, Token
from tests import test_app
from app.mixins import TestMixin
from app import db


class TestEffectApi(TestMixin):
    endpoint = '/api/effects'

    def setup(self):
        db.create_all()

    def test_get_empty(self):
        raw = test_app.get(self.endpoint)
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check res is 200
        eq_(raw.status_code, 200)
        # no users yet, right?
        eq_(len(resp), 0)

    def test_duplicate_post(self):
        poll = Poll(name="poll test")
        question = Question(text="question test", poll_id=poll.id)
        token = Token(
            name='token',
            value=0,
            maximum=50,
            minimum=-50,
            poll_id=poll.id
        )
        db.session.add(poll)
        db.session.add(question)
        db.session.add(token)
        db.session.commit()
        question_endpoint = ('/api/questions/%d/effects' % question.id)
        resource = Effect(value=5, question_id=question.id, token_id=token.id)

        # make a effect
        raw = test_app.post(question_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # try to resubmit
        raw = test_app.post(question_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 500)

    def test_post(self):
        poll = Poll(name="poll test")
        question = Question(text="question test", poll_id=poll.id)
        token = Token(
            name='token',
            value=0,
            maximum=50,
            minimum=-50,
            poll_id=poll.id
        )
        db.session.add(poll)
        db.session.add(question)
        db.session.add(token)
        db.session.commit()
        question_endpoint = ('/api/questions/%d/effects' % question.id)
        resource = Effect(value=5, question_id=question.id, token_id=token.id)

        # make a questions
        raw = test_app.post(question_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)

        eq_(raw.status_code, 201)
        # check raw.data
        resp = json.loads(raw.data)
        eq_(resp["value"], resource.value)
        eq_(resp["question_id"], resource.question_id)
        eq_(resp["token_id"], resource.token_id)

        # check raw from poll endpoint
        raw = test_app.get(question_endpoint)
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)

        # 200?
        eq_(raw.status_code, 200)
        # one question, right?
        eq_(len(resp), 1)

    def test_get_id(self):
        poll = Poll(name="poll test")
        question = Question(text="question test", poll_id=poll.id)
        token = Token(
            name='token',
            value=0,
            maximum=50,
            minimum=-50,
            poll_id=poll.id
        )
        db.session.add(poll)
        db.session.add(question)
        db.session.add(token)
        db.session.commit()
        question_endpoint = ('/api/questions/%d/effects' % question.id)
        resource = Effect(value=5, question_id=question.id, token_id=token.id)

        # make a question
        raw = test_app.post(question_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)
        # check raw.data
        resp = json.loads(raw.data)
        # get a specific question
        raw = test_app.get(self.endpoint + ('/%s' % resp['id']))
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check each field
        eq_(resp["value"], resource.value)
        eq_(resp["question_id"], resource.question_id)

        eq_(resp["token_id"], resource.token_id)
