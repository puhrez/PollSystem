import json
from nose.tools import eq_
from app.models import Poll
from tests import test_app
from app.mixins import TestMixin


class TestPollApi(TestMixin):
    resource = Poll(name="test1")
    endpoint = '/api/polls'

    def test_get_empty(self):
        raw = test_app.get(self.endpoint)
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check res is 200
        eq_(raw.status_code, 200)
        # no users yet, right?
        eq_(len(resp), 0)

    def test_duplicate_post(self):
        # make a user
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        self.check_content_type(raw.headers)
        print raw.data
        eq_(raw.status_code, 201)

        # try to resubmit
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        print raw.data
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 500)

    def test_post(self):
        # amke a poll
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)
        eq_(resp['name'], self.resource.name)

        # check for persistence
        raw = test_app.get(self.endpoint)
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)

        # 200?
        eq_(raw.status_code, 200)
        eq_(len(resp), 1)

    def test_get_id(self):
        # make a poll
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)

        # get a specific poll
        raw = test_app.get(self.endpoint + ('/%s' % resp['id']))
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)

        # check name
        eq_(resp['name'], self.resource.name)
