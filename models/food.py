from peewee import Model, IntegerField, ForeignKeyField
from .db import db
from .user import User
from .restaurant import Restaurant


class Food(Model):
    user = ForeignKeyField(User, backref="orders")
    restaurant = ForeignKeyField(Restaurant, backref="orders")
    evaluation = IntegerField()
    time_h = IntegerField()

    class Meta:
        database = db
