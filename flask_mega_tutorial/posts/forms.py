from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    body = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Post')
