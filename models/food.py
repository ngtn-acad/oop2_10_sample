from peewee import Model, IntegerField, ForeignKeyField,DateField,TextField
from .db import db
from .user import User
from .restaurant import Restaurant


class Food(Model):
    user = ForeignKeyField(User, backref="orders")
    restaurant = ForeignKeyField(Restaurant, backref="orders")
    food = TextField()
    evaluation = IntegerField()
    time = DateField(formats='%Y-%m-%d %H:%M:%S')

    class Meta:
        database = db
