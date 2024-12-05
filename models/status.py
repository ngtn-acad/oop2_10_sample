from peewee import Model, CharField, IntegerField
from .db import db

class Status(Model):
    name = CharField()
    item = CharField()
    hp = IntegerField()
    at = IntegerField()
    df = IntegerField()

    class Meta:
        database = db