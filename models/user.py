from peewee import Model, CharField
from .db import db

class User(Model):
    name = CharField()
    gender = CharField()

    class Meta:
        database = db