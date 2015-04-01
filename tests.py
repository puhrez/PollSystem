#!flask/bin/python

"""
TODO:
Write tests for:
Token creation
Effect creation

Adding several questions to a Poll
Adding several tokens to a Poll
Adding several effects to a question

Accessing a poll's questions
Acessing a question's poll
Accessing a poll's tokens
Accessing a token's poll
Accessing a question's effects
Accessing an effect's token
"""

import unittest
from app.models import User, Poll, Token, Question, Effect
from app import db, app

class ModelTests(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://polladmin:pollMaster@localhost/pollapptest'
    self.app = app.test_client()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_poll_user_relationship(self):
    # create test users
    u = User(email="test@example", name="John")
    u2 = User(email="test2@example", name="Susan")
    db.session.add(u)
    db.session.add(u2)
    db.session.commit()

    #create test polls
    p = Poll(name="test1")
    p.admins.append(u)
    p2 = Poll(name="test2")
    p2.admins.append(u2)
    p3 = Poll(name="test3")
    p3.admins.append(u)
    p3.admins.append(u2)

    db.session.add(p)
    db.session.add(p2)
    db.session.commit()

    #register a user to a poll
    u.polls.append(p2)
    u2.polls.append(p2)

    db.session.add(u)
    db.session.commit()

    u = db.session.query(User).get(u.id)
    u2 = db.session.query(User).get(u2.id)

    assert u.polls_admin.count() == 2
    assert p2 in u2.polls.all()
    assert p in u.polls_admin.all()
    assert u2.polls_admin.count() == 2
    assert u.polls.count() + u.polls_admin.count() == 3
    assert u2.polls.count() == 1

if __name__ == '__main__':
  unittest.main()
