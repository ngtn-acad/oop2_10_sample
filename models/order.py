from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .customer import Customer
from .goods import Goods


class Order(Model):
    user = ForeignKeyField(Customer, backref="orders")
    product = ForeignKeyField(Goods, backref="orders")
    order_date = DateTimeField()

    class Meta:
        database = db
