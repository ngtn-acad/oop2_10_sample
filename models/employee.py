from peewee import *
from .db import db
from models import Hire

# モデル定義
class Employee(Model):
    employee_id = AutoField()  # 主キー（自動生成される一意の識別子）
    hire_id = ForeignKeyField(Hire,backref="employees")
    first_name = CharField(max_length=10)  # 名（最大10文字）
    last_name = CharField(max_length=10)  # 姓（最大10文字）
    gender = CharField(max_length=5)  # 性別（最大5文字）
    date_of_birth = DateField()  # 生年月日
    email = CharField(max_length=100, unique=True)  # メールアドレス（一意）
    phone_number = CharField(max_length=20, unique=True)  # 電話番号（一意）
    address = TextField()  # 住所

    @property
    def hire(self):
        return self.hire_id

    class Meta:
        database = db  # 使用するデータベースを指定