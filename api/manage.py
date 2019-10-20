import os
from flask import Flask
from flask_script import Manager

from app import create_app, db

if 'PRODUCTION' in os.environ and os.environ['PRODUCTION']:
    app = create_app('production')
elif 'TESTING' in os.environ and os.environ['TESTING']:
    app = create_app('testing')
else:
    app = create_app('dev')

manager = Manager(app)

if __name__ == '__main__':
    manager.run()
