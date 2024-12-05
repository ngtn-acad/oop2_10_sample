from peewee import SqliteDatabase
from .db import db
from .customer import Customer
from .goods import Goods
from .order import Order

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    Customer,
    Goods,
    Order,
]


# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()
