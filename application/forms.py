__author__ = "Musketeer Liu"


from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    id = StringField('id', validators=[DataRequired()])
    ingredients = TextAreaField(
        'ingredients', validators=[DataRequired()],
        render_kw={"placeholder": "Please type in your ingredients, separated by comma"})
    submit = SubmitField('Predict')
