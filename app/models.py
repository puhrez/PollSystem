from app import db
from datetime import datetime
"""
TODO:
add as_dict() methods http://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json/11884806#11884806
"""

"""
This is our helper table to create the many-to-many relationship
between users and polls
"""
memberships = db.Table('memberships',
  db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
  db.Column('poll_id', db.Integer, db.ForeignKey('polls.id'))
)

class User(db.Model):
  """
  This class represents a single user who has:
    a unique id,
    a unique email,
    a password,
    a name
    and a set of polls
  """
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(64), index=True, unique=True)
  password = db.Column(db.String(10))
  name = db.Column(db.String(64))
  polls = db.relationship('Poll', secondary=memberships, lazy='dynamic',
    backref=db.backref('users', lazy='dynamic'))

  def __repr__(self):
    #Prints out a string representing the user
    return '<User %r>' % (self.name)

class Poll(db.Model):
  """
  This class represents a single poll which has:
    a unique id,
    a name,
    a created data,
    a set of questions
    a set of users (refered to from the users backref)
    a set of tokens
  """
  __tablename__ = 'polls'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(65))
  timestamp = db.Column(db.DateTime, server_default=db.func.now())
  questions = db.relationship('Question', backref='poll', lazy='dynamic')
  tokens = db.relationship('Token', backref='poll', lazy='dynamic')

  def __repr__(self):
    return "<Polls %r>" % (self.name)

class Question(db.Model):
  __tablename__ = 'questions'
  """
  This class represents a single question which has:
    a unique id,
    a string, text, which is the question itself
    a set of effects
  """
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(250))
  poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
  effects = db.relationship('Effect', backref='question', lazy='dynamic')

  def __repr__(self):
    return "<Question %r>" % (self.text)

class Effect(db.Model):
  __tablename__ = 'effects'
  """
  This class represents a single effect that a question has on a token:
    a unique id,
    a positive or negative value
    a token it affects
  """
  id = db.Column(db.Integer, primary_key=True)
  value = db.Column(db.Integer)
  question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
  token_id = db.Column(db.Integer, db.ForeignKey('tokens.id'))

  def __repr__(self):
    return "<Effect %d on token-id %d>" % (self.value, self.token)

class Token(db.Model):
  __tablename__ = 'tokens'
  """
  This class represents a single token that has:
  a unique id,
  a maximum value,
  a minimum value,
  whether it is an upperbound
  whether it is a lowerbound
  a text which is the token
  """
  id = db.Column(db.Integer, primary_key=True)
  poll_id = db.Column(db.Integer, db.ForeignKey('polls.id'))
  is_upperbound = db.Column(db.Boolean)
  is_lowerbound = db.Column(db.Boolean)
  maximum = db.Column(db.Integer)
  minimum = db.Column(db.Integer)
  text = db.Column(db.String(100), unique=True)

