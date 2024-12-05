from peewee import Model, CharField, DecimalField
from .db import db

class Weapon(Model):
    name = CharField()
    attribute = CharField()
    atackpower = DecimalField()

    class Meta:
        database = db