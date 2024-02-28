from flask import Flask, render_template, flash, redirect, url_for
from main import app
from main.forms import RegisterForm

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', content=name)


@app.route('/register', methods=['POST', 'GET'])
def register():
    forms = RegisterForm()
    if forms.validate_on_submit():
        flash(f'account created {forms.username.data}')
        return redirect(url_for('home'))
    return render_template('register.html', forms=forms)
    