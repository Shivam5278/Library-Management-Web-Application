from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired


class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Submit')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')

class AddMemberForm(FlaskForm):
    mem_id = StringField('ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddTransactionForm(FlaskForm):
    mem_id = StringField('ID', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    book = StringField('Book', validators=[DataRequired()])
    rent = IntegerField('Rent', validators=[DataRequired()])
    rdate = DateField('Date', validators=[DataRequired()], format = '%Y-%m-%d' )
    submit = SubmitField('Submit')
