from peewee import Model, CharField, IntegerField
from .db import db

class Product(Model):
    number = CharField()
    like = IntegerField()
    language = CharField()

    class Meta:
        database = db