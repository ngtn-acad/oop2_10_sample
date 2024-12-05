from flask import Blueprint, render_template, request, redirect, url_for
from models import Product, User, Review

# Blueprintの作成
review_bp = Blueprint('review', __name__, url_prefix='/reviews')


@review_bp.route('/')
def list():
    reviews = Review.select()
    return render_template('review_list.html', title='レビュー一覧', items=reviews)


@review_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        product_id = request.form['product_id']
        review_data = request.form['review_data']
        review_comment = request.form['review_comment']
        Review.create(user=user_id, product=product_id, review_data=review_data)
        return redirect(url_for('review.list'))
    
    users = User.select()
    products = Product.select()
    return render_template('order_add.html', users=users, products=products)