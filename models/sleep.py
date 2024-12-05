from peewee import Model, IntegerField, ForeignKeyField
from .db import db
from .user import User

class Sleep(Model):
    start = IntegerField()
    end = IntegerField()
    user = ForeignKeyField(User, backref='sleeps')

    class Meta:
        database = db