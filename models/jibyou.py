from peewee import Model, ForeignKeyField, DateTimeField, BooleanField
from .db import db
from .user import User
from .product import Product

class Jibyou(Model):
    user = ForeignKeyField(User, backref='jibyou')
    check = BooleanField()

    class Meta:
        database = db
