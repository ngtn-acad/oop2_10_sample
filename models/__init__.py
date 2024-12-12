from peewee import SqliteDatabase
from .db import db
from .user import User
from .test import Test
from .sleep import Sleep


# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Test,
    Sleep,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()