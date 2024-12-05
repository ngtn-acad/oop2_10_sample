from peewee import Model, CharField, DecimalField
from .db import db

class Product(Model):
    name = CharField()
    price = DecimalField()
    categori = DecimalField()
    class Meta:
        database = db