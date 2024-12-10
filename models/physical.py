from peewee import ForeignKeyField,DoubleField,BooleanField,CharField,Model
from .db import db
from .user import User
from .task import Task

class Physical(Model):
    user_id = ForeignKeyField(User, backref='user_id')
    task = ForeignKeyField(Task, backref='task')
    # temp = DoubleField()
    bad_good = BooleanField(default=True)
    bad_content = CharField()
    class Meta:
        database = db
