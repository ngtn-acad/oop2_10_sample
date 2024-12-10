from peewee import Model, CharField, ForeignKeyField, PrimaryKeyField
from .db import db
from .user import User

class Task(Model):
    user_id = ForeignKeyField(User, backref='tasks')
    task_name = CharField()
    task_content = CharField()

    class Meta:
        database = db