from peewee import SqliteDatabase
from .db import db
from .user import User
from .product import Product
from .order import Order
from .jibyou import Jibyou
from .appointment import Appointment
from .medical_condition import MedicalCondition
# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Product,
    Order,
    Jibyou,
    Appointment,
    MedicalCondition
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()