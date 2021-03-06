import os
from flask import Flask
from flask_script import Manager

from app import create_app, db

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
