from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .customer import Customer
from .goods import Goods


class Order(Model):
    customer = ForeignKeyField(Customer, backref="orders")
    goods = ForeignKeyField(Goods, backref="orders")
    order_date = DateTimeField()

    class Meta:
        database = db
