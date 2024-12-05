from peewee import Model, CharField, IntegerField
from .db import db

class Customer(Model):
    name = CharField()
    number = IntegerField()

    class Meta:
        database = db