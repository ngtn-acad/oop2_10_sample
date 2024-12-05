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
        # 選択されたユーザーと装備を取得
        selected_user = User.get(User.id == user_id)
        selected_item = Item.get(Item.id == product_id)
        
        # ユーザーのHPと装備のHPを計算または表示
        total_hp = int(selected_user.hp + selected_item.hitpoint)
        total_at = int(selected_user.at + selected_item.attack)
        total_df = int(selected_user.df + selected_item.defence)

        Status.create(user=user_id, product=product_id, hp=total_hp, at=total_at, df=total_df)
        return redirect(url_for('status.list'))
    
    users = User.select()
    items = Item.select()
    return render_template('status_add.html', users=users, items=items, total_hp=total_hp, total_at=total_at, total_df=total_df)

@status_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(status_id):
    status = Status.get_or_none(Status.id == status_id)
    if not status:
        return redirect(url_for('status.list'))

    if request.method == 'POST':
        status.user = request.form['user_id']
        status.product = request.form['product_id']
        # 選択されたユーザーと装備を取得
        selected_user = User.get(User.id == status.user)
        selected_item = Item.get(Item.id == status.product)
        
        # ユーザーのHPと装備のHPを計算または表示
        total_hp = int(selected_user.hp + selected_item.hitpoint)
        total_at = int(selected_user.at + selected_item.attack)
        total_df = int(selected_user.df + selected_item.defence)

        status.save()
        return redirect(url_for('status.list'))

    users = User.select()
    items = Item.select()
    return render_template('status_edit.html', users=users, items=items, total_hp=total_hp, total_at=total_at, total_df=total_df)