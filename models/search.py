from peewee import Model, CharField, DecimalField
from .db import db

class Search(Model):
    name = CharField()
    a = DecimalField()

    class Meta:
        database = db