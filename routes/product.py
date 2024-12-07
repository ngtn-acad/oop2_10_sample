from flask import Blueprint, render_template, request, redirect, url_for
from models import Product

# Blueprintの作成
product_bp = Blueprint('product', __name__, url_prefix='/products')


@product_bp.route('/')
def list():
    products = Product.select()
    return render_template('product_list.html', title='製品一覧', items=products)


@product_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        Product.create(name=name, price=price)
        return redirect(url_for('product.list'))
    
    return render_template('product_add.html')








@product_bp.route('/edit/<int:food_number>', methods=['GET', 'POST'])
def edit(product_id):
    product = Product.get_or_none(Product.id == product_id)
    if not food_number:
        return redirect(url_for('food_number.list'))

    if request.method == 'POST':
        food_numer.name = request.form['name']
        food_number.price = request.form['price']
        food_number.save()
        return redirect(url_for('food_number.list'))

    return render_template('product_edit.html', product=product)


@product_bp.route('/edit/<int:drink_number>', methods=['GET', 'POST'])
def edit(product_id):
    product = Product.get_or_none(Product.id == product_id)
    if not drink_number:
        return redirect(url_for('drink_number.list'))

    if request.method == 'POST':
        drink_number.name = request.form['name']
        drink_number.price = request.form['price']
        drink_number.save()
        return redirect(url_for('product.list'))

    return render_template('product_edit.html', product=product)