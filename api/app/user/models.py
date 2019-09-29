import datetime

from app import db

from app.utils.serializer import Serializer
from app.utils.uuid import generateUUID

class User(db.Model, Serializer):
    __tablename__ = 'users'
    __public__ = ['id', 'firstname', 'lastname', 'email', 'age', 'gender']

    id = db.Column(db.Unicode, primary_key=True, unique=True, default=generateUUID)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    age = db.Column(db.SmallInteger, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def __init__(self, firstname, lastname, email, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.age = age
        self.gender = gender

    def __repr__(self):
        return "<ID: {}>".format(self.id)
