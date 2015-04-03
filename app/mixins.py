from nose.tools import eq_
from app import db


class ModelMixin(object):
    """
    Mixin class for model's shared functions
    """
    def as_dict(self):
        """
        returns the object as a dictionary
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class TestMixin(object):
    endpoint = ""

    def check_content_type(self, headers):
        eq_(headers['Content-Type'], 'application/json')

    def setup(self):
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()
