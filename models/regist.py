from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .user import User
from .subject import Subject

class Regist(Model):
    user = ForeignKeyField(User, backref='orders')
    subject = ForeignKeyField(Subject, backref='orders')
    regist_date = DateTimeField()

    class Meta:
        database = db
