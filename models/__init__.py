from .db import db
from .user import User
from .tag import Tag
from .article import Article
from .product import Product
from .order import Order
from .postData import PostData

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Article,
    Tag,
    Product,
    Order,
    PostData
    
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()
    
    # データの初期値を登録
    #tagを複数登録
    
    tagArray = ['Python', 'Ruby', 'Java', 'PHP', 'JavaScript']
    
    for tag in tagArray:
        Tag.create(word=tag)

        
    