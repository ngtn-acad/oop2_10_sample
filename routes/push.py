from flask import Blueprint, render_template, request, redirect, url_for
from models import Order, User, Product, Article, PostData, Tag
from datetime import datetime

# Blueprintの作成
order_bp = Blueprint('push', __name__, url_prefix='/push')


@order_bp.route('/')
def list():
    
    postDatas = PostData.select()
    return render_template('order_list.html', title='投稿一覧', items=postDatas )


@order_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        article_id = request.form['article_title']
        
        article = Article.get_or_none(Article.id == article_id)
        tag = article.tag
        created_at = datetime.now()
        PostData.create(user=user_id,  title=article.title,tag = tag , created_at=created_at)
        return redirect(url_for('push.list'))
    
    users = User.select()
    articles = Article.select()
    return render_template('order_add.html', users=users, articles=articles)


@order_bp.route('/edit/<int:postData_id>', methods=['GET', 'POST'])
def edit(postData_id):
    article = PostData.get_or_none(PostData.id == postData_id)
    if not article:
        return redirect(url_for('push.list'))

    if request.method == 'POST':
        article.user = request.form['user_id']
        article.title = request.form['title']
        article.save()
        return redirect(url_for('push.list'))

    users = User.select()
    articles = Article.select()
    return render_template('order_edit.html', articles = articles, users=users , article=article)
