from flask import Blueprint, render_template, request, redirect, url_for
from models import User, Item, Status

# Blueprintの作成
status_bp = Blueprint('status', __name__, url_prefix='/status')


@status_bp.route('/')
def list():
    
    # データ取得
    statuses = Status.select()

    return render_template('status_list.html', title='ステータス一覧', items=statuses)


@status_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        Status.create(user=user_id, product=product_id)
        return redirect(url_for('stutas.list'))
    
    users = User.select()
    items = Item.select()
    return render_template('status_add.html', users=users, items=items)

@status_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(status_id):
    status = Status.get_or_none(Status.id == status_id)
    if not status:
        return redirect(url_for('order.list'))

    if request.method == 'POST':
        status.user = request.form['user_id']
        status.product = request.form['product_id']
        status.save()
        return redirect(url_for('status.list'))

    users = User.select()
    items = Item.select()
    return render_template('order_edit.html', status=status, users=users, items=items)