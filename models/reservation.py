from peewee import Model, CharField, DecimalField
from .db import db

class Reservation(Model):
    name = CharField()
    food_name = CharField()
    drink_name = CharField()
    price = DecimalField()

    class Meta:
        database = db