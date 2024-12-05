from flask import Blueprint, render_template, request, redirect, url_for
from models import Article, Tag,User
from datetime import datetime

# Blueprintの作成
article_bp = Blueprint('article', __name__, url_prefix='/article')


@article_bp.route('/')
def list():
    articles = Article.select()
    return render_template('product_list.html', title='記事一覧', items=articles)


@article_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        title = request.form['title']
        tag_id = request.form['tag_id']
        users = User.select()

        user_id = ""

        created_at = datetime.now()
        Article.create(user = user_id,title=title, tag=tag_id , created_at = created_at)
        
        return redirect(url_for('article.list'))
    
    
    tags = Tag.select()

    
    return render_template('product_add.html',tags = tags)


@article_bp.route('/edit/<int:article_id>', methods=['GET', 'POST'])
def edit(article_id):
    article = Article.get_or_none(Article.id == article_id)
    if not article:
        return redirect(url_for('product.list'))

    if request.method == 'POST':
        article.user = request.form['title']
        article.tag = request.form['tag_id']
        article.save()
        return redirect(url_for('product.list'))
    
    #users = User.select()
    #articles = Article.select()

    return render_template('product_edit.html', article=article)