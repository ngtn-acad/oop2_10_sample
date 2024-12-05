from peewee import Model, ForeignKeyField, DateTimeField,CharField,IntegerField
from .db import db

class Tag(Model):
    word = CharField()

    class Meta:
        database = db
