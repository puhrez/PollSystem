from app import api
from resources.res_users import UserView, UserList
from resources.res_effects import EffectView, EffectList, EffectQuestionList
from resources.res_tokens import TokenView, TokenList, TokenPollList
from resources.res_polls import PollView, PollList
from resources.res_questions import QuestionPollList, QuestionView
from resources.res_questions import QuestionList

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
"""
specific collection endpoints
"""
api.add_resource(
    TokenPollList,
    '/api/polls/<string:poll_id>/questions')
api.add_resource(
    QuestionPollList,
    '/api/polls/<string:poll_id>/tokens')
api.add_resource(
    EffectQuestionList,
    '/api/polls/<string:poll_id>/effects')
