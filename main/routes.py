from flask import render_template, flash, redirect, url_for,session, abort, request
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Message
from sqlalchemy.sql.expression import func
from main import app, db,  mail
from main.forms import RegisterForm, LoginForm, PostForm, CommentForm
from .models import User, Post, Comment
from main import bcrypt



def check_user(model, pk):
    post = model.query.get_or_404(pk)

    if current_user != post.user:
            abort(403)
    return post


@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', content=name)


@app.route('/register', methods=['POST', 'GET'])
def register():
    forms = RegisterForm()
    if forms.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(forms.password.data)
        user = User(username=forms.username.data, email=forms.email.data, password=hashed_password)
        
        with mail.connect() as conn:
            msg = Message(f'Account created. Don\'t worry youre account is not hacked im just practicing coding by sending emails', sender='justpracticingflask', recipients=[forms.email.data], body=f'Account created for {forms.username.data}')
            mail.send(msg)

        db.session.add(user)
        db.session.commit()
        flash(f'account created {forms.username.data}')
        return redirect(url_for('home'))
    return render_template('register.html', forms=forms)
    

    
@app.route('/login', methods=['POST', 'GET'])
def login():
    forms = LoginForm()
    if forms.validate_on_submit():
        user = User.query.filter_by(username=forms.username.data).first()
        if user and bcrypt.check_password_hash(user.password, forms.password.data):
            login_user(user, remember=True)
            print('Login succesfully')
            return redirect(url_for('home'))
    return render_template('login.html', forms=forms)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/create/post', methods=['POST', 'GET'])
@login_required
def create_post():
    forms = PostForm()
    if forms.validate_on_submit(): 
        post = Post(user_id=session['_user_id'], title=forms.title.data, hashtag=forms.hashtag.data, body=forms.body.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_post.html', forms=forms)



@app.route('/post/<pk>', methods=['GET', 'POST'])
def single_post(pk):
    post = Post.query.get(pk)
    return render_template('single_post.html', post=post)


@app.route('/post/<pk>/edit', methods=['GET', 'POST', 'PATCH'])
def edit_post(pk):
    post = check_user(Post, pk)
    forms = PostForm()


    if forms.validate_on_submit():
        post.user_id= session['_user_id']
        post.title = forms.title.data
        post.body = forms.body.data
        db.session.commit()
        return redirect(url_for('single_post', pk=pk))
    elif request.method == "GET":
        return render_template('edit_post.html', post=post, forms=forms)


@app.route('/post/<pk>/delete')
def delete_post(pk):
    post = check_user(Post, pk)
    db.session.delete(post)
    db.session.commit()
    return render_template('home.html')

@app.route('/post/<pk>/comment/add', methods=['POST', "GET"])
def create_comment(pk):
    post = Post.query.get_or_404(pk)
    forms = CommentForm()
    if forms.validate_on_submit():
        comment = Comment(author_id=session['_user_id'], content=forms.content.data, post_id=str(pk))
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('single_post', pk=pk))
    return render_template('create_comment.html', forms=forms)