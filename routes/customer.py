from flask import Blueprint, render_template, request, redirect, url_for
from models.customer import Customer

# Blueprintの作成
customer_bp = Blueprint('customer', __name__, url_prefix='/customers')


@customer_bp.route('/')
def list():
    
    # データ取得
    customers = Customer.select()

    return render_template('custoer_list.html', title='客リスト', items=customers)