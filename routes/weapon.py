from flask import Blueprint, render_template, request, redirect, url_for
from models import Weapon

# Blueprintの作成
weapon_bp = Blueprint('weapon', __name__, url_prefix='/weapons')


@weapon_bp.route('/')
def list():
    weapons = Weapon.select()
    return render_template('product_list.html', title='製品一覧', items=weapons)


@weapon_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        Weapon.create(name=name, price=price)
        return redirect(url_for('product.list'))
    
    return render_template('product_add.html')


@weapon_bp.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit(product_id):
    product = Weapon.get_or_none(Weapon.id == product_id)
    if not product:
        return redirect(url_for('product.list'))

    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.save()
        return redirect(url_for('product.list'))

    return render_template('product_edit.html', product=product)