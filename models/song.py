from peewee import Model, CharField
from .db import db

class Song(Model):
    song = CharField()
    artist = CharField()

    class Meta:
        database = db