
from flask import Flask

app = Flask(__name__)
from.import views

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
####Move toconfig.py####

app.config['SECRET_KEY'] = '\xa5\x11\x06\x03q\xb4\xe5\x08o\xdb\xba9\x8fxT\xa9\xf6\xe6\x1bi\tW\x03\xd6'
