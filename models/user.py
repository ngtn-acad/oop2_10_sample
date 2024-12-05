from peewee import Model, TextField, IntegerField
from .db import db


class User(Model):
    student_id = TextField(unique=True)
    name = TextField()
    gender = TextField()
    age = IntegerField()

    class Meta:
        database = db
