from peewee import SqliteDatabase
from .db import db
from .user import User
from .subject import Subject
from .regist import Regist

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Subject,
    Regist,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()