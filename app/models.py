from app import db
from sqlalchemy.schema import UniqueConstraint
import bcrypt
from mixins import ModelMixin
"""
This is our helper table to create the many-to-many relationship
between users and polls
"""
memberships = db.Table(
    'memberships',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('poll_id', db.Integer, db.ForeignKey('poll.id'))
)

"""
This is our helper table to create the many-to-many relationship
between users and polls as administrators
"""
administrators = db.Table(
    'administrators',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('poll_id', db.Integer, db.ForeignKey('poll.id'))
)


class User(db.Model, ModelMixin):
    """
      This class represents a single user who has:
        a unique id,
        a unique email,
        a password,
        a name
        and a set of polls
      Has a many-to-many relationship with Poll
      Has a many-to-many relationship with Poll as admin
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(250))
    name = db.Column(db.String(64))
    polls = db.relationship(
        'Poll', secondary=memberships, lazy='dynamic',
        backref=db.backref('users', lazy='dynamic')
    )
    polls_admin = db.relationship(
        'Poll', secondary=administrators, lazy='dynamic',
        backref=db.backref('admins', lazy='dynamic')
    )

    def __init__(self, name, password, email):
        self.name = name
        self.password = bcrypt.hashpw(password, bcrypt.gensalt(10))
        self.email = email

    def password_match(self, password):
        return bcrypt.hashpw(password, self.password) == self.password

    def __repr__(self):
        """
        Prints out a string representing the user
        """
        return '<User %r>' % (self.name)


class Poll(db.Model, ModelMixin):
    """
      This class represents a single poll which has:
        a unique id,
        a name,
        a created data,
        a set of questions
        a set of users (refered to from the users backref)
        a set of tokens
      Has a many-to-many relationship with User, backref is 'users'
      Has a many-to-many relationship with User as admin, backref is 'admins'
      Has a one-to-many relationship with Question
      Has a one-to-many relationship with Token
    """
    __tablename__ = "poll"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65))
    tokens = db.relationship('Token', backref='poll', lazy='dynamic')
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    questions = db.relationship('Question', backref='poll', lazy='dynamic')

    def __repr__(self):
        return "<Polls %r>" % (self.name)


class Question(db.Model, ModelMixin):
    """
      This class represents a single question which has:
        a unique id,
        a string, text, which is the question itself
        a set of effects
      Has a one-to-many relatinoship with Effect
    """
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250))
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    effects = db.relationship('Effect', backref='questions', lazy='dynamic')

    def __repr__(self):
        return "<Question %r>" % (self.text)


class Effect(db.Model, ModelMixin):
    __tablename__ = 'effect'
    """
    This class represents a single effect that a question has on a token:
    a unique id,
    a positive or negative value
    a token it affects
    Has a backref to its Question as 'question'
    Has a reference to its respective Token
    """
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    token_id = db.Column(db.Integer, db.ForeignKey('token.id'))

    def __repr__(self):
        return "<Effect %d on token-id %d>" % (self.value, self.token)


class Token(db.Model, ModelMixin):
    __tablename__ = 'token'
    __table_args__ = (
        UniqueConstraint('poll_id', 'text', name='poll_id_text_uix'),
    )
    """
    This class represents a single token that has:
    a unique id,
    a maximum value,
    a minimum value,
    a text which is the token
    Has a backrefernce to is parent poll as'poll'
    """
    id = db.Column(db.Integer, primary_key=True)
    poll_id = db.Column(db.Integer, db.ForeignKey('poll.id'))
    value = db.Column(db.Integer, default=0)
    maximum = db.Column(db.Integer)
    minimum = db.Column(db.Integer)
    text = db.Column(db.String(100), unique=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__tabe__.columns}

    def __repr__(self):
        return "<Token id %d>" % (self.value, self.token)
