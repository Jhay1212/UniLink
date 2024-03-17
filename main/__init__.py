from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_alembic import Alembic


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
alembic = Alembic()
login_manager = LoginManager(app)


login_manager.init_app(app)
db = create_db()
alembic.init_app(app)


   

app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'rjhay1070@gmail.com'
app.config['MAIL_PASSWORD'] = 'byiu jval olau crhy '
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
# mail.init_app(app)

from main import routes