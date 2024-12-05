from peewee import SqliteDatabase
from .db import db
from .user import User
from .customer import customer
from .order import Order
from .customer import Customer

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    customer,
    Order,
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()