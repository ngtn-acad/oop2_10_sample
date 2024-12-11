from peewee import Model, CharField, IntegerField
from .db import db

class PartTimer(Model):
    name = CharField()
    category = CharField()
    hourlypay = IntegerField()

    class Meta:
        database = db