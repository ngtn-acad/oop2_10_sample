from peewee import Model, CharField, DecimalField
from .db import db

class Product(Model):
    kind = CharField()
    name = CharField()
    food = CharField()

    class Meta:
        database = db