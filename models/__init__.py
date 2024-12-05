from peewee import SqliteDatabase
from .db import db
from .character import Character
from .weapon import Weapon
from .quest import Quest

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    Character,
    Weapon,
    Quest,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()