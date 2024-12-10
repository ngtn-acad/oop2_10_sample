from peewee import SqliteDatabase
from .db import *
from .user import User
from .product import Product
from .order import Order
from .task import Task
from .physical import Physical


# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Product,
    Order,
    Task,
    Physical,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()