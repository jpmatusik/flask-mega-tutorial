from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError

from flask_mega_tutorial.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(4, 20)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(7, 40)])
    password = PasswordField('password', validators=[DataRequired(), Length(4, 20)])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(form, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError('This username has been taken. Try another one.')

    def validate_email(form, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('This email has been taken. Try another one.')



class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')
