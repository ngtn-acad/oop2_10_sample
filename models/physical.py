from peewee import ForeignKeyField, DecimalField, BooleanField, CharField, Model
from .db import db
from .user import User

class Physical(Model):
    user = ForeignKeyField(User, backref='physicals')
    temp = DecimalField()  # 固定小数点
    bad_good = BooleanField(default=True)
    bad_content = CharField()
    class Meta:
        database = db
