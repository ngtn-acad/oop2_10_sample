from flask import Blueprint, render_template, request, redirect, url_for
from models import Character

# Blueprintの作成
character_bp = Blueprint('character', __name__, url_prefix='/chraacters')


@character_bp.route('/')
def list():
    
    # データ取得
    characters = Character.select()

    return render_template('user_list.html', title='ユーザー一覧', items=characters)


@character_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        Character.create(name=name, gender=gender)
        return redirect(url_for('character.list'))
    
    return render_template('user_add.html')


@character_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = Character.get_or_none(Character.id == user_id)
    if not user:
        return redirect(url_for('user.list'))

    if request.method == 'POST':
        user.name = request.form['name']
        user.gender = request.form['gender']
        user.save()
        return redirect(url_for('character.list'))

    return render_template('user_edit.html', user=user)