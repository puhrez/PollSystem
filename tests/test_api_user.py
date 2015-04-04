import json
from nose.tools import eq_
from app.models import User
from tests import test_app
from app.mixins import TestMixin


class TestUserApi(TestMixin):
    resource = User(email="test1@example.com", name="test1", password='pie')
    endpoint = '/api/users'

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
        eq_(raw.status_code, 201)

        # try to resubmit
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        print raw.data
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 500)

    def test_post(self):
        # make a user
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)
        eq_(resp["email"], self.resource.email)
        eq_(resp["name"], self.resource.name)

        raw = test_app.get(self.endpoint)
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)

        # 200?
        eq_(raw.status_code, 200)
        # one user, right?
        eq_(len(resp), 1)

    def test_get_id(self):
        # make a user
        raw = test_app.post(self.endpoint, data=self.resource.as_dict())
        self.check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)
        # get a specific user
        raw = test_app.get(self.endpoint + ('/%s' % resp['id']))
        self.check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check each field
        eq_(resp['email'], self.resource.email)
        eq_(resp['name'], self.resource.name)
