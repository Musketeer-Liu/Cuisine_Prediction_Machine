from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    recipe = StringField('Recipe', validators=[DataRequired()])
