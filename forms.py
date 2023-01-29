from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class getText(FlaskForm):
    text = StringField("text")
    submit = SubmitField("submit")