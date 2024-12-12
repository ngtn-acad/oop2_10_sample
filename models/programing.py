from peewee import Model, CharField, IntegerField
from .db import db

class Programing(Model):
    number = CharField()
    like = IntegerField()
    language = CharField()

    class Meta:
        database = db