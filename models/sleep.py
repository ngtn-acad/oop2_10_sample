from peewee import Model, CharField, IntegerField
from .db import db

class Sleep(Model):
    name = CharField()
    start = IntegerField()
    end = IntegerField()

    class Meta:
        database = db