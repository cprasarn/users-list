import os
import json
import datetime
from flask import Flask, g
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from config import config

api = Api()

db = SQLAlchemy()

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


def create_before_request(app):
    def before_request():
        g.db = db
    return before_request


def create_app(config_name):
    """Create an application."""
    app = Flask(__name__)
    app.debug = True
    app.config.from_object(config[config_name])

    # User
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    # Add the before request handler
    app.before_request(create_before_request(app))

    # JSONEncoder
    app.json_encoder = JSONEncoder

    # API
    CORS(app)
    api.init_app(app)

    # Database
    db.init_app(app)

    # This does the binding
    app.app_context().push()

    # Initialize DB
    db.create_all()

    return app

