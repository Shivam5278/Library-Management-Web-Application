from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
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
