from peewee import Model, CharField, IntegerField
from .db import db

class Challenger(Model):
    name = CharField()
    age = IntegerField()
    gender = IntegerField()

    class Meta:
        database = db