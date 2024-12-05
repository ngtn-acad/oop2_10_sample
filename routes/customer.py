from flask import Blueprint, render_template, request, redirect, url_for
from models import Customer

# Blueprintの作成
customer_bp = Blueprint('customer', __name__, url_prefix='/customers')


@customer_bp.route('/')
def list():
    
    # データ取得
    customer = Customer.select()

    return render_template('customer_list.html', title='客一覧', customers=customer)


@customer_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        table = request.form['table']
        Customer.create(table=table)
        return redirect(url_for('customer.list'))
    
    return render_template('customer_add.html')


@customer_bp.route('/edit/<int:customer_id>', methods=['GET', 'POST'])
def edit(customer_id):
    customer = Customer.get_or_none(Customer.id == customer_id)
    if not customer:
        return redirect(url_for('customer.list'))

    if request.method == 'POST':
        customer.table = request.form['table']
        customer.save()
        return redirect(url_for('customer.list'))

    return render_template('customer_edit.html', customer=customer)