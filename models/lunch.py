from peewee import Model, CharField, DecimalField
from .db import db

class Lunch(Model):
    number = CharField()
    lunch_place = DecimalField()

    class Meta:
        database = db