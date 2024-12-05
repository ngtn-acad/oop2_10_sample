from peewee import Model, CharField, IntegerField
from .db import db

class Customer(Model):
    # id = IntegerField(primary_key=True)
    # table = IntegerField()
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db