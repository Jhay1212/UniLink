from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():

    app = Flask('__main__', template_folder='main/template')
    app.config['SECRET_KEY'] = '7a84ec5ac2294106cf137011fe57b60a5c74f9e6ba6e002b'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    app.app_context().push()
    print()
    return app

app = create_app()

def create_db():
    db = SQLAlchemy()
    db.init_app(app)
    return db

db = create_db()

from main import routes