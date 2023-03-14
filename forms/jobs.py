from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    work_size = StringField('Длительность', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена')

    team_leader = StringField('Руководитель', validators=[DataRequired()])
    submit = SubmitField('Применить')
