import json
from nose.tools import eq_
from app.models import Question, Poll
from tests import test_app
from app.mixins import TestMixin
from app import db


class TestUserApi(TestMixin):
    endpoint = '/api/questions'

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
        db.session.add(poll)
        db.session.commit()
        poll_endpoint = ('/api/polls/%d/questions' % poll.id)
        resource = Question(text="question", poll_id=poll.id)

        # make a question
        raw = test_app.post(poll_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # try to resubmit
        raw = test_app.post(poll_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 500)

    def test_post(self):
        poll = Poll(name="poll test")
        db.session.add(poll)
        db.session.commit()
        poll_endpoint = ('/api/polls/%d/questions' % poll.id)
        resource = Question(text="question", poll_id=poll.id)

        # make a questions
        raw = test_app.post(poll_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)
        eq_(resp["text"], resource.text)

        # check raw from poll endpoint
        raw = test_app.get(poll_endpoint)
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)

        # 200?
        eq_(raw.status_code, 200)
        # one question, right?
        eq_(len(resp), 1)

    def test_get_id(self):
        poll = Poll(name="poll test")
        db.session.add(poll)
        db.session.commit()
        poll_endpoint = ('/api/polls/%d/questions' % poll.id)
        resource = Question(text="question", poll_id=poll.id)

        # make a question
        raw = test_app.post(poll_endpoint, data=resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)
        # check raw.data
        resp = json.loads(raw.data)
        # get a specific question
        raw = test_app.get(self.endpoint + ('/%s' % resp['id']))
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check each field
        eq_(resp['text'], resource.text)
