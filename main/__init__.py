from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


def create_app():

    app = Flask('__main__', template_folder='main/template')
    app.config['SECRET_KEY'] = '7a84ec5ac2294106cf137011fe57b60a5c74f9e6ba6e002b'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


    app.app_context().push()
    print()
    return app


def create_db():
    db = SQLAlchemy()
    db.init_app(app)
    return db


app = create_app()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
db = create_db()

from main import routes