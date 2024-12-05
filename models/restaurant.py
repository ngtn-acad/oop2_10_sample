from peewee import Model, TextField
from .db import db


class Restaurant(Model):
    name = TextField(unique=True)
    address = TextField()

    class Meta:
        database = db
