from peewee import *
from .db import db

class Hire(Model):
    hire_id = AutoField()  # 主キー（自動生成される一意の識別子）
    hire_date = DateField()  # 入社した日付
    job_title = CharField()  # マネージャー、エンジニア、営業担当など
    department_name = CharField()  #部署を識別する
    employment_type = CharField()  # 正社員、契約社員、アルバイトなど
    salary = IntegerField()
    status = CharField()  # 在職中、退職済み、求職中など
    

    class Meta:
        database = db  # 使用するデータベースを指定
