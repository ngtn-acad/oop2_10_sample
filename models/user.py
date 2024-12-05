from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    user_id = IntegerField()
    username = CharField()
    age = IntegerField()

    class Meta:
        database = db