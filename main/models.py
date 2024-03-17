from main import db, login_manager
from datetime import datetime
from flask_login import UserMixin



@login_manager.user_loader
def user_loader(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    email =  db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)
 
    
    def __repr__(self) -> str:
        return f'User {self.username}'.title()

    def __str__(self):
        return f'{self.username}'
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    body = db.Column(db.String(256), nullable=False)
    hashtag = db.Column(db.String(80), default=None)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now())
    comments = db.relationship('Comment', backref='post')

    def __str__(self) -> str:
        return self.title
    
    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    
