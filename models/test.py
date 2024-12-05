from peewee import Model, CharField, IntegerField, ForeignKeyField
from .db import db
from .user import User  # Userモデルをインポート

class Test(Model):
    name = CharField()  # 教科名
    score = IntegerField()  # 点数
    user = ForeignKeyField(User, backref='tests')  # Userモデルとのリレーション

    class Meta:
        database = db  # データベース接続を指定