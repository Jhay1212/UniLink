from main import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    email =  db.Column(db.String(120), unique=True)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self) -> str:
        return f'User {self.username}'.title()
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(60), nullable=False)
    body = db.Column(db.String(256), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)
    comments = db.relationship('Comment', backref='')

class Comment(db.Model):
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    
