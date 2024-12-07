from peewee import Model, DateTimeField, CharField
from .db import db

class Appointment(Model):
    appointment_datetime = DateTimeField()
    patient_name = CharField()
    class Meta:
        database = db 