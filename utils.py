from wtforms import StringField, SubmitField, validators
from flask_wtf import FlaskForm

class QueryForm(FlaskForm):
    querytext = StringField('Ask a question', [validators.InputRequired('Please ask a question')])
    submit = SubmitField('Submit')
