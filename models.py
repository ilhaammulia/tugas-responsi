from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
import wtforms


class LoginForm(FlaskForm):
    email = wtforms.StringField('Email Address', validators=[InputRequired(
        'Email Address harus diisi.'), Email('Email Address tidak sesuai.')])
    password = wtforms.PasswordField(
        'Password', validators=[InputRequired('Password harus diisi.')])
    remember = wtforms.BooleanField('Remember me')
    login = wtforms.SubmitField('Log In')
