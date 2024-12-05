from flask import Blueprint, render_template, request, redirect, url_for
from models import Product

# Blueprintの作成
product_bp = Blueprint('goods', __name__, url_prefix='/goods')


@product_bp.route('/')
def list():
    products = Product.select()
    return render_template('goods_list.html', title='商品一覧', items=products)


@product_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        Product.create(name=name, price=price)
        return redirect(url_for('goods.list'))
    
    return render_template('goods_add.html')


@product_bp.route('/edit/<int:goods_id>', methods=['GET', 'POST'])
def edit(goods_id):
    product = Product.get_or_none(Product.id == goods_id)
    if not product:
        return redirect(url_for('goods.list'))

    if request.method == 'POST':
        product.name = request.form['name']
        product.price = request.form['price']
        product.save()
        return redirect(url_for('goods.list'))

    return render_template('goods_edit.html', goods=product)