from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .user import User
from .subject import Subject

class Regist(Model):
    user = ForeignKeyField(User, backref='regists')
    subject = ForeignKeyField(Subject, backref='regists')
    regist_date = DateTimeField()

    class Meta:
        database = db
