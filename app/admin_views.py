from app import admin, models, db
from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField, SelectField
import bcrypt


class UserView(ModelView):
    column_list = ('name', 'email')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('password',)

    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.new_password = PasswordField(u'New Password')
        return form_class

    def on_model_change(self, form, model):
        if len(form.new_password.data):
            model.password = bcrypt.hashpw(
                form.new_password.data.encode('utf-8'),
                bcrypt.gensalt(10)
            )

    def __init__(self, session, **kwargs):
        super(UserView, self).__init__(models.User, session, **kwargs)


class EffectView(ModelView):
    column_auto_select_related = True

    def __init__(self, session, **kwargs):
        super(EffectView, self).__init__(models.Effect, session, **kwargs)

class QuestionView(ModelView):

    def __init__(self, session, **kwargs):
        super(QuestionView, self).__init__(models.Question, session, **kwargs)

class PollView(ModelView):
    form_excluded_columns = ('timestamp', )
    inline_models = (models.Token, )

    def __init__(self, session, **kwargs):
        super(PollView, self).__init__(models.Poll, session, **kwargs)

admin.add_view(EffectView(db.session))
admin.add_view(PollView(db.session))
admin.add_view(UserView(db.session))
admin.add_view(QuestionView(db.session))
