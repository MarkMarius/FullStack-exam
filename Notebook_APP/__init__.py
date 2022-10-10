import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from notebook_app.models import User
from notebook_app.models import db


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'qwqedfdfgwergrwgewrggewgwegwegwegew'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basedir = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join('static', 'notes_images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "signin"
login_manager.login_message_category = "info"

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

from notebook_app import routes