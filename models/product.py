from peewee import Model, CharField, DecimalField,DateField
from .db import db

class Product(Model):
    name = CharField()
    author = CharField()
    

    class Meta:
        database = db