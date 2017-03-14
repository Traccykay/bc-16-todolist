# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_script import Manager, Shell

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    db.init_app(app)

    # temporary route
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    login_manager.init_app(app)
    login_manager.login_message = "You need to be logged in."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    

    return app
