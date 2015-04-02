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

  def test_poll_question_relationship(self):
    #creating polls
    p = Poll(name='test1')
    p2 = Poll(name='test2')
    db.session.add(p)
    db.session.add(p2)
    db.session.commit()

    #creating questions
    q = Question(text='question1')
    q2 = Question(text='question2')
    q3 = Question(text='question3')
    q4 = Question(text='question4')

    ##adding them to polls
    p.questions.append(q)
    p.questions.append(q2)
    p.questions.append(q3)
    p2.questions.append(q4)

    db.session.add(p)
    db.session.add(p2)
    db.session.commit()

    p = db.session.query(Poll).get(p.id)
    p2 = db.session.query(Poll).get(p2.id)

    assert p.questions.count() == 3
    assert p2.questions.count() == 1
    assert q in p.questions.all()
    assert q4 not in p.questions.all()
    assert q4 in p2.questions.all()
    assert q4.poll == p2
    assert q3.poll == p

  def test_poll_token_relationship(self):
    #creating polls
    p = Poll(name='test1')
    p2 = Poll(name='test2')
    db.session.add(p)
    db.session.add(p2)
    db.session.commit()

    #creating tokens
    t = Token(text="token1")
    t2 = Token(text="token2")
    db.session.add(t)
    db.session.add(t2)
    db.session.commit()
    p.tokens.append(t)
    p2.tokens.append(t2)

    db.session.add(p)
    db.session.add(p2)
    db.session.commit()

    p = db.session.query(Poll).get(p.id)
    p2 = db.session.query(Poll).get(p2.id)
    assert p.tokens.count() == 1
    assert t in p.tokens.all()
    assert t not in p2.tokens.all()
    assert t.poll is p
    assert t2.poll is not p

  def test_question_effect_token_relationship(self):
    #creating questions
    q = Question(text='question1')
    db.session.add(q)
    db.session.commit()

    #creating tokens, value is 0 by default, just making it explicit
    t = Token(text="token1", value=0)
    t2 = Token(text="token2", value=0)
    db.session.add(t)
    db.session.add(t2)
    db.session.commit()

    #creating effects
    e = Effect(value=3, question_id=q.id, token_id=t.id)
    e2 = Effect(value=-4, question_id=q.id, token_id=t2.id)
    db.session.add(e)
    db.session.add(e2)
    db.session.commit()

    #checking relationships
    q = db.session.query(Question).get(e.question_id)
    t = db.session.query(Token).get(e.token_id)
    t2 = db.session.query(Token).get(e2.token_id)
    assert e and e2 in q.effects.all()
    assert t.value + e.value == 3
    assert t2.value + e2.value == -4

  def test_effects_affect_tokens(self):
    #creating tokens, value is 0 by default, just making it explicit
    t = Token(text="token1", value=0)
    t2 = Token(text="token2", value=0)
    db.session.add(t)
    db.session.add(t2)
    db.session.commit()

    #creating effects
    e = Effect(value=3, token_id=t.id)
    e2 = Effect(value=-4, token_id=t2.id)
    db.session.add(e)
    db.session.add(e2)
    db.session.commit()

    #changing values
    t.value += e.value
    t2.value += e2.value
    db.session.add(t)
    db.session.add(t2)
    db.session.commit()

    #getting tokens from db again  to ensure persistence of changes
    t = db.session.query(Token).get(e.token_id)
    t2 = db.session.query(Token).get(e2.token_id)

    assert t.value == 3
    assert t2.value == -4

