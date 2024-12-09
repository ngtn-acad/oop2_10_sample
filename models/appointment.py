from peewee import Model, DateTimeField, ForeignKeyField, CharField
from .db import db
from .user import User

class Appointment(Model):
    appointment_datetime = DateTimeField()
    patient = ForeignKeyField(User, backref='appointments')  # UserモデルへのForeignKey
    department = CharField()  # 診療科フィールドを追加

    class Meta:
        database = db 