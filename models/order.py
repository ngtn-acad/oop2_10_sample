from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .customer import Customer
from .product import Product

class Order(Model):
    user = ForeignKeyField(Customer, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    order_date = DateTimeField()

    class Meta:
        database = db
