from peewee import Model, CharField, IntegerField, PrimaryKeyField
from .db import db

class User(Model):
    username = CharField()
    age = IntegerField()

    class Meta:
        database = db
