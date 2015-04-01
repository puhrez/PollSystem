#!flask/bin/python

"""
TODO:
Write tests for:
User creation
Poll creation
Question creation
Token creation
Effect creation

Adding several polls to a User
Adding several users to a Poll
Adding several questions to a Poll
Adding several tokens to a Poll
Adding several effects to a question

Accessing a user's polls
Accessing a poll's users
Accessing a poll's questions
Acessing a question's poll
Accessing a poll's tokens
Accessing a token's poll
Accessing a question's effects
Accessing an effect's token
"""

import unittest
from app.models import User, Poll, Token, Question, Effect
from app import db

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

  def test_user_create(self):
    u = User(email="test@example", name="John")
  
  def test_poll_create(self):
  def test_question_create(self):
  def test_token_create(self):
  def test_effect_create(self):

