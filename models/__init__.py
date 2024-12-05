from peewee import SqliteDatabase
from .db import db
from .user import User
from .product import Product
from .role import Role

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Product,
    Role,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()