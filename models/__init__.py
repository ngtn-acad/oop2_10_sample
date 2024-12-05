from peewee import SqliteDatabase
from .db import db
from .challenger import Challenger
from .song import Song
from .score import Score

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
	Challenger,
    Song,
    Score,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()