from flask import Blueprint, render_template, request, redirect, url_for
from models import Physical, User, Task
from models.db import db
from datetime import datetime

# Blueprintの作成
physical_bp = Blueprint('physical', __name__, url_prefix='/physicals')


@physical_bp.route('/')
def list():
    physical = Physical.select()
    print(physical)
    return render_template('physical_list.html', title='体調一覧', items=physical)


@physical_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_tb = request.form['user_id']
        task_tb = request.form['task_tb']
        physical_tb = datetime.now()
        Physical.create(user=user_tb, task=task_tb, physical_date=physical_tb)
        return redirect(url_for('physical_list.html'))
    
    users = User.select()
    task= Task.select()
    return render_template('physical_add.html', users=users, task=task)


@physical_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(physical_id):
    physical = Physical.get_or_none(Physical.id == physical_id)
    if not physical:
        return redirect(url_for('physical_list.html'))

    if request.method == 'POST':
        physical.user_id = request.form['user_id']
        physical.product = request.form['product_id']
        physical.save()
        return redirect(url_for('physical_list.html'))

    users = User.select()
    task = Task.select()
    return render_template('physical_edit.html', physical=physical, users=users, task=task)
