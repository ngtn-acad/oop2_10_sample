from peewee import Model, CharField, ForeignKeyField
from .db import db
from .user import User

class MedicalCondition(Model):
    user = ForeignKeyField(User, backref='medical_conditions')
    condition = CharField()  # 持病の内容

    class Meta:
        database = db 