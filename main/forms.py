from flask_wtf import FlaskForm
from wtforms_alchemy import ModelForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError
from .models import User, Post, Comment

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=6, max=16), DataRequired()])
    email = EmailField('Email', validators=[DataRequired(),Email() ])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')
        if len(username.data) < 6:
            raise ValidationError('Username must have at least 6 characters.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already taken')
        
    def validate_password(self, password):
        if len(password.data) < 8:
            raise ValidationError('Password is too short')
        
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Length(min=6, max=16), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me', default=False)
    submit = SubmitField('Login')
       
# class PostForm(ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['user_id', 'date_posted']

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Length(min=0, max=120), DataRequired()])
    body = StringField("What's in your mind.", validators=[Length(min=1, max=256), DataRequired()])
    hashtag = StringField("Hashtag", validators=[Length(max=80)], default=None)
    submit = SubmitField("Post")


class CommentForm(FlaskForm):
    content = StringField('Add Comment', validators=[Length(min=1, max=100), DataRequired()])
    submit = SubmitField("Comment")
