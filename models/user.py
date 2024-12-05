from peewee import Model, CharField, IntegerField
from .db import db

class User_tb(Model):
    user_id = IntegerField()
    username = CharField()
    age = IntegerField()

    class Meta:
        database = db