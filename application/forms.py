from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    recipe = TextAreaField(
        'Recipe', validators=[DataRequired()],
        render_kw={"placeholder": "Please type in your ingredients, separated by comma"})
    submit = SubmitField('Predict')
