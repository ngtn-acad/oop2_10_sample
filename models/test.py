from peewee import Model, CharField, IntegerField
from .db import db

class Test(Model):
    name = CharField()  # 教科名
    score = IntegerField()  # 点数

    class Meta:
        database = db  # データベース接続を指定
