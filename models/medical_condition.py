from peewee import Model, CharField, ForeignKeyField
from models.db import db
from models.user import User

class MedicalCondition(Model):
    user = ForeignKeyField(User, backref='medical_conditions')
    condition = CharField()  # 持病の内容

    class Meta:
        database = db
        table_name = 'medical_condition' 