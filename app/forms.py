from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, ValidationError
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=500)])
    poster = FileField('Poster', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    