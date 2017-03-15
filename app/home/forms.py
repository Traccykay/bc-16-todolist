from flask_wtf import FlaskForm
from wtforms import (BooleanField, DateField, StringField,
                     SubmitField, TextField, ValidationError)


class ListForm(FlaskForm):

    list_name = StringField('List Name', validators=[DataRequired])
    submit = SubmitField('Save')

class CardsForm(FlaskForm):

    card_name = StringField('Card Title', validators=[DataRequired])
    description = TextField('Description')
    submit = SubmitField('Save')

class ItemsForm(FlaskForm):

    item_name = StringField('Item Name', validators=[DataRequired])
    due_date = DateField('Due Date', validators=[DataRequired])
    done = BooleanField('Done')
    submit = SubmitField('Save')
