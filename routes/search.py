from flask import Blueprint, render_template, request, redirect, url_for
from models import Search

# Blueprintの作成
search_bp = Blueprint('user', __name__, url_prefix='/searches')


@search_bp.route('/')
def list():
    
    # データ取得
    users = Search.select()

    return render_template('search_list.html', title='検索一覧', items=searches)


@search_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        Search.create(name=name, age=age)
        return redirect(url_for('search.list'))
    
    return render_template('search_add.html')


@search_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(search_id):
    user = Search.get_or_none(Search.id == search_id)
    if not search:
        return redirect(url_for('search.list'))

    if request.method == 'POST':
        search.name = request.form['name']
        search.age = request.form['age']
        search.save()
        return redirect(url_for('search.list'))

    return render_template('search_edit.html', search=search)