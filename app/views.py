from app import api
from resources import UserView, UserList
from resources import EffectView, EffectList, EffectQuestionList
from resources import TokenView, TokenList, TokenPollList, PollView, PollList
from resources import QuestionPollList, QuestionList, QuestionView

"""
View endpoints
"""
api.add_resource(QuestionView, '/api/questions/<string:question_id>')
api.add_resource(TokenView, '/api/tokens/<string:token_id>')
api.add_resource(PollView, '/api/polls/<string:poll_id>')
api.add_resource(EffectView, '/api/effects/<string:effect_id>')
api.add_resource(UserView, '/api/users/<string:user_id>')

"""
collection endpoints
"""
api.add_resource(QuestionList, '/api/questions')
api.add_resource(TokenList, '/api/tokens')
api.add_resource(PollList, '/api/polls')
api.add_resource(EffectList, '/api/effects')
api.add_resource(UserList, '/api/users')
api
"""
specific collection endpoints
"""
api.add_resource(
    TokenPollList,
    '/api/polls/<string:poll_id>/<string:question_id>')
api.add_resource(
    QuestionPollList,
    '/api/polls/<string:poll_id>/<string:token_id>')
api.add_resource(
    EffectQuestionList,
    '/api/polls/<string:poll_id>/<string:token_id>')
