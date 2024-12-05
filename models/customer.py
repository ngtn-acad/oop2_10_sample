from peewee import Model, CharField, DecimalField
from .db import db

class Customer(Model):
    name = CharField()
    numPeople = DecimalField()

    class Meta:
        database = db