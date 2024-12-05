from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    name = CharField()
    studentNumber = CharField()
    gender = CharField()
    

    class Meta:
        database = db