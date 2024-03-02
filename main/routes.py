from flask import Flask, render_template, flash, redirect, url_for
from main import app
from main.forms import RegisterForm
from .models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', content=name)


@app.route('/register', methods=['POST', 'GET'])
def register():
    forms = RegisterForm()
    user = ''
    if forms.validate_on_submit():
        user = User(username=forms.data['username'], email=forms.data['email'], password=forms.data['password'])
        from main import db
        db.session.add(user)
        db.session.commit()
        flash(f'account created {forms.username.data}')
        print(forms.data)
        return redirect(url_for('home'))
    print('not valid')
    print(forms.errors)
    return render_template('register.html', forms=forms)
    