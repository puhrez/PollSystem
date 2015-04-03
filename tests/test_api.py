import nose
import json
from nose.tools import *
from app.models import User
from tests import test_app
from app import db
import bcrypt


def check_content_type(headers):
        eq_(headers['Content-Type'], 'application/json')


class TestUserApi():
    u = User(email="test1@example.com", name="test1", password='pie')

    def setup(self):
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_get_empty(self):
        raw = test_app.get('/api/users')
        check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check res is 200
        eq_(raw.status_code, 200)
        # no users yet, right?
        eq_(len(resp), 0)

    def test_post(self):
        # make a user
        raw = test_app.post('/api/users', data=self.u.as_dict())
        check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)
        eq_(resp["email"], "test1@example.com")
        eq_(resp["name"], "test1")

        raw = test_app.get('/api/users')
        check_content_type(raw.headers)
        resp = json.loads(raw.data)

        # 200?
        eq_(raw.status_code, 200)
        # one user, right?
        eq_(len(resp), 1)

    def test_get_id(self):
        # make a user
        raw = test_app.post('/api/users', data=self.u.as_dict())
        check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # check raw.data
        resp = json.loads(raw.data)
        # get a specific user
        raw = test_app.get('/api/users/%s' % resp['id'])
        check_content_type(raw.headers)
        resp = json.loads(raw.data)
        # check each field
        eq_(resp['email'], 'test1@example.com')
        eq_(resp['name'], 'test1')

    def test_duplicate_post(self):
        # make a user
        raw = test_app.post('/api/users', data=self.u.as_dict())
        check_content_type(raw.headers)
        eq_(raw.status_code, 201)

        # try to resubmit
        raw = test_app.post('/api/users', data=self.u.as_dict())
        print raw.data
        check_content_type(raw.headers)
        eq_(raw.status_code, 500)
