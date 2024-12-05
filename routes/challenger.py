from flask import Blueprint, render_template, request, redirect, url_for
from models import Challenger

# Blueprintの作成
challenger_bp = Blueprint('challenger', __name__, url_prefix='/challengers')


@challenger_bp.route('/')
def list():
    
    # データ取得
    challengers = Challenger.select()

    return render_template('challenger_list.html', title='チャンレジャー一覧', items=challengers)


@challenger_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        Challenger.create(name=name, age=age,gender=gender)
        return redirect(url_for('challenger.list'))
    
    return render_template('challenger_add.html')


@challenger_bp.route('/edit/<int:challenger_id>', methods=['GET', 'POST'])
def edit(challenger_id):
    challenger = Challenger.get_or_none(Challenger.id == challenger_id)
    if not challenger:
        return redirect(url_for('challenger.list'))

    if request.method == 'POST':
        challenger.name = request.form['name']
        challenger.age = request.form['age']
        challenger.save()
        return redirect(url_for('challenger.list'))

    return render_template('challenger_edit.html', challenger=challenger)