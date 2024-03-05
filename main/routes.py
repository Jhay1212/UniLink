from flask import render_template, flash, redirect, url_for,session
from flask_login import login_user
from main import app
from main.forms import RegisterForm, LoginForm, PostForm
from .models import User, Post
from main import bcrypt
from datetime import datetime
from main import db

@app.route('/')
def home():
    posts = [{
        'content': 'loremn12',
        'author': 'zeef',
        'date': datetime.now(),
        'image': 'ts'
        
    },
    {
        'content': 'frieren',
        'author': 'zeef0',
        'date': datetime.now()
        
    }]
    print(session)
    return render_template('home.html', posts=posts)


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', content=name)


@app.route('/register', methods=['POST', 'GET'])
def register():
    forms = RegisterForm()
    user = ''
    if forms.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(forms.password.data)
        user = User(username=forms.username.data, email=forms.email.data, password=hashed_password)

        db.session.add(user)
        db.session.commit()
        flash(f'account created {forms.username.data}')
        return redirect(url_for('home'))
    print('not valid')
    print(forms.errors)
    return render_template('register.html', forms=forms)
    

    
@app.route('/login', methods=['POST', 'GET'])
def login():
    forms = LoginForm()
    if forms.validate_on_submit():
        user = User.query.filter_by(email=forms.email.data).first()
        if user and bcrypt.check_password_hash(user.password, forms.password.data):
            login_user(user, remember=forms.remember.data)
            print('Login succesfully')
            return redirect(url_for('home'))
    print(forms.errors)
    return render_template('login.html', forms=forms)




@app.route('/create/post', methods=['POST', 'GET'])
def create_post():
    forms = PostForm()
    if forms.validate_on_submit():
        
        post = Post(user_id=session['_user_id'], title=forms.title.data, body=forms.body.data)
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('create_post.html', forms=forms)