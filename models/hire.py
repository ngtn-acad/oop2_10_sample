from peewee import *
from .db import db

class Hire(Model):
    hire_date = DateField()  # 入社した日付
    job_title = CharField()  # マネージャー、エンジニア、営業担当など
    department_id = CharField()  #　部署を識別するための外部キー
    employment_type = CharField()  # 正社員、契約社員、アルバイトなど
    date_of_birth = CharField()  # 基本給または年収
    status = CharField()  # 在職中、退職済み、求職中など
    

    class Meta:
        database = db  # 使用するデータベースを指定

