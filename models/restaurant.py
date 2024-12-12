from peewee import Model, TextField, FloatField
from .db import db


class Restaurant(Model):
    name = TextField(unique=True)
    address = TextField()
    lat = FloatField()
    long = FloatField()

    class Meta:
        database = db
