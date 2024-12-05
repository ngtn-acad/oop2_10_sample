from flask import Blueprint, render_template, request, redirect, url_for
from models import User

# Blueprintの作成
user_bp = Blueprint('user', __name__, url_prefix='/users')


@user_bp.route('/')
def list():
    
    # データ取得
    users = User.select()

    return render_template('user_list.html', title='キャラクター一覧', items=users)


@user_bp.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']  # 性別を取得
        User.create(name=name, gender=gender)  # 性別を保存
        return redirect(url_for('user.list'))
    
    return render_template('user_add.html')


@user_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = User.get_or_none(User.id == user_id)
    if not user:
        return redirect(url_for('user.list'))

    if request.method == 'POST':
        user.name = request.form['name']
        user.gender = request.form['gender']
        user.save()
        return redirect(url_for('user.list'))

    return render_template('user_edit.html', user=user)