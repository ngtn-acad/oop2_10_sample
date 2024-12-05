from peewee import Model, CharField, DecimalField, ForeignKeyField
from .db import db
from .user import User

class Task(Model):
    user = ForeignKeyField(User, backref='tasks')
    type = CharField()
    content = DecimalField()

    class Meta:
        database = db