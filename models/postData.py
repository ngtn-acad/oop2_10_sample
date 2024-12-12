from peewee import Model, ForeignKeyField, DateTimeField , CharField
from .db import db
from .user import User
from .tag import Tag
from .article import Article


class PostData(Model):
    user = ForeignKeyField(User, backref='articles')
    article = ForeignKeyField(Article, backref='articles')
    tag = ForeignKeyField(Tag, backref='tags')
    created_at = DateTimeField()
    
    

    class Meta:
        database = db