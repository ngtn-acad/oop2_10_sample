from peewee import Model, CharField, IntegerField, ForeignKeyField
from .db import db
from .user import User  # Userモデルをインポート

class Test(Model):
    japanese = IntegerField()  # 点数
    math = IntegerField()  # 点数
    english = IntegerField()  # 点数
    user = ForeignKeyField(User, backref='tests')  # Userモデルとのリレーション

    class Meta:
        database = db  # データベース接続を指定