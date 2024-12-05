from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    name = CharField()
    start = IntegerField()
    end = IntegerField()
    

    class Meta:
        database = db