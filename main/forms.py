from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=6, max=16), DataRequired()])
    email = EmailField('Email', validators=[DataRequired(),Email() ])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

    