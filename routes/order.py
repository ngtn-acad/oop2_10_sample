from flask import Blueprint, render_template, request, redirect, url_for
from models import User, Product , Role
from datetime import datetime

# Blueprintの作成
role_bp = Blueprint('role', __name__, url_prefix='/roles')


@role_bp.route('/')
def list():
    roles = Role.select()
    print(roles)
    return render_template('order_list.html', title='飼育表', items=roles)#htmlファイル名を変える


@role_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        keeper_id = request.form['keeper_id']
        animal_id = request.form['animal_name']
        regist_date = datetime.now()
        Role.create(keeper=keeper_id, animal=animal_id, regist_date=regist_date)
        return redirect(url_for('role.list'))
    
    keepers = User.select()
    animals = Product.select()
    return render_template('order_add.html', keepers=keepers, animals=animals)


@role_bp.route('/edit/<int:role_id>', methods=['GET', 'POST'])
def edit(role_id):
    role = Role.get_or_none(Role.id == role_id)
    if not role:
        return redirect(url_for('role.list'))

    if request.method == 'POST':
        role.user = request.form['keeper_id']
        role.product = request.form['animal_id']
        role.save()
        return redirect(url_for('role.list'))

    users = User.select()
    products = Product.select()
    return render_template('order_edit.html', role=role, users=users, products=products)
