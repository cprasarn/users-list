import os
from flask import Flask, g
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import config

api = Api()

db = SQLAlchemy()
ma = Marshmallow()

def create_before_request(app):
    def before_request():
        g.db = db
    return before_request


def create_app(config_name='testing'):
    """Create an application."""
    app = Flask(__name__)
    app.config.from_object(config[os.environ.get('FLASK_ENV', config_name)])

    # User
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    # Add the before request handler
    app.before_request(create_before_request(app))

    # API
    CORS(app)
    api.init_app(app)

    # Database
    db.init_app(app)

    # Marshmallow
    ma.init_app(app)

    # This does the binding
    app.app_context().push()

    # Initialize DB
    db.create_all()

    return app

