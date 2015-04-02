from app import db, api
from flask.ext.restful import reqparse, abort, Resource

class UserList(Resource):
  """
  This resource represents the collection of all users
  """
  def get(self):
    pass
  def post(self):
    pass

class UserSimple(Resource):
  """
  This resource represents a single user
  """
  def get(self, user_id):
    pass
  def put(self, user_id):
    pass
  def delete(self, user_id):
    pass

class PollList(Resource):
  """
  This resource represents the collection of all Polls
  """
  def get(self):
    pass
  def post(self):
    pass

class PollSimple(Resource):
  """
  This resource represents a single Poll
  """
  def get(self, poll_id):
    pass
  def put(self, poll_id):
    pass
  def delete(self, poll_id):
    pass

class QuestionPollList(Resource):
  """
  This resource represents the collection of Questions for a specific Poll
  """
  def get(self, poll_id):
    pass
  def post(self, poll_id):
    pass

class QuestionList(Resource):
  """
  This resource represents the collection of Questions
  """
  def get(self):
    pass
  def post(self):
    pass

class QuestionSimple(Resource):
  """
  This resource represents a single Question
  """
  def get(self, question_id):
    pass
  def put(self, question_id):
    pass
  def delete(self, question_id):
    pass

class TokenPollList(Resource):
  """
  This resource represents the collection of Tokens for a specific Poll
  """
  def get(self, poll_id):
    pass
  def post(self, poll_id):
    pass

class TokenList(Resource):
  """
  This resource represents the collection of Tokens
  """
  def get(self):
    pass
  def post(self):
    pass

class TokenSimple(Resource):
  """
  This resource represents a single Token
  """
  def get(self, token_id):
    pass
  def put(self, token_id):
    pass
  def delete(self, token_id):
    pass

class EffectQuestionList(Resource):
  """
  This resource represents a collection of effects for a specific question
  """
  def get(self, question_id):
    pass
  def post(self, question_id):
    pass

class EffectList(Resource):
  """
  This resource represents the collection of effects
  """
  def get(self):
    pass
  def post(self):
    pass

class EffectSimple(Resource):
  """
  This resource represents a specifc effects
  """
  def get(self, effect_id):
    pass
  def put(self, effect_id):
    pass
  def delete(self, effect_id):
    pass

#simple endpoints
app.add_resource(QuestionSimple, '/api/questions/<string:question_id>')
app.add_resource(TokenSimple, '/api/tokens/<string:token_id>')
app.add_resource(PollSimple, '/api/polls/<string:poll_id>')
app.add_resource(EffectSimple, '/api/effects/<string:effect_id>')
app.add_resource(UserSimple, '/api/users/<string:user_id>')


#collection endpoints
app.add_resource(QuestionList, '/api/questions')
app.add_resource(TokenList, '/api/tokens')
app.add_resource(PollList, '/api/polls')
app.add_resource(EffectList, '/api/effects')
app.add_resource(UserList, '/api/users')



#specific collection endpoints

app.add_resource(TokenPollList, '/api/polls/<string:poll_id>/<string:question_id>')
app.add_resource(QuestionPollList, '/api/polls/<string:poll_id>/<string:token_id>')
app.add_resource(EffectQuestionList, '/api/polls/<string:poll_id>/<string:token_id>')
