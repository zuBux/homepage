from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired


class PostForm(Form):
  title = StringField('Title', validators=[DataRequired()])
  body = TextAreaField('Body', validators=[DataRequired()])
  category = SelectField('Category', \
  											choices=[('1', 'Blog'), ('2', 'Advisory')], \
  											validators=[DataRequired()])
  date = DateField('Date', validators=[DataRequired()])


class LoginForm(Form):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])
