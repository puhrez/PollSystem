from app import admin, models, db
from flask_admin.contrib.sqla import ModelView
from wtforms import PasswordField, TextField
import bcrypt


class UserView(ModelView):
    column_list = ('name', 'email')
    column_searchable_list = ('name', 'email')
    form_excluded_columns = ('password',)

    def scaffold_form(self):
        form_class = super(UserView, self).scaffold_form()
        form_class.new_password = PasswordField('New Password')
        return form_class

    def on_model_change(self, form, model):
        if len(form.new_password):
            model.password = bcrypt.hashpw(
                form.new_password,
                bcrypt.gensalt(10)
            )


class TokenView(ModelView):
    def scaffold_form(self):
        form_class = super(TokenView, self).scaffold_form()
        return form_class


class QuestionView(ModelView):
    inline_models = (TokenView(models.Effect, db.session), )


class PollView(ModelView):
    form_excluded_columns = ('timestamp', )
    inline_models = (models.Token, QuestionView(models.Question, db.session))


admin.add_view(PollView(models.Poll, db.session))
admin.add_view(UserView(models.User, db.session))
admin.add_view(QuestionView(models.Question, db.session))
