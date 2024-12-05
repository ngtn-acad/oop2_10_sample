from peewee import Model, ForeignKeyField, IntegerField
from .db import db
from .challenger import Challenger
from .song import Song

class Score(Model):
    challenger = ForeignKeyField(Challenger, backref='scores')
    song = ForeignKeyField(Song, backref='scores')
    score = IntegerField()

    class Meta:
        database = db
