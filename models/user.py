from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    name = CharField()
    student_id = CharField()

    class Meta:
        database = db