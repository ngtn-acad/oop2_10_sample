from flask import Blueprint, render_template, request, redirect, url_for
from models import Quest, Character, Weapon
from datetime import datetime

# Blueprintの作成
quest_bp = Blueprint('quest', __name__, url_prefix='/orders')


@quest_bp.route('/')
def list():
    orders = Quest.select()
    return render_template('order_list.html', title='注文一覧', items=orders)


@quest_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        order_date = datetime.now()
        Quest.create(user=user_id, product=product_id, order_date=order_date)
        return redirect(url_for('order.list'))
    
    characters = Character.select()
    weapons = Weapon.select()
    return render_template('order_add.html', users=characters, products=weapons)


@quest_bp.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit(order_id):
    quest = Quest.get_or_none(Quest.id == order_id)
    if not quest:
        return redirect(url_for('order.list'))

    if request.method == 'POST':
        quest.user = request.form['user_id']
        quest.product = request.form['product_id']
        quest.save()
        return redirect(url_for('order.list'))

    characters = Character.select()
    weapons = Weapon.select()
    return render_template('order_edit.html', order=quest, users=characters, products=weapons)
