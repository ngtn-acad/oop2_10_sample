from peewee import Model, CharField, DecimalField
from .db import db

class Weapon(Model):
    name = CharField()
    price = DecimalField()

    class Meta:
        database = db