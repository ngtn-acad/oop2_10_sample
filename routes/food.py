from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant,Food,User
from datetime import datetime

# Blueprintの作成
food_bp = Blueprint('food', __name__, url_prefix='/foods')


@food_bp.route('/')
def list():
    foods = Food.select()
    return render_template('food_list.html', title='食べたもの一覧',foods=foods)


@food_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        restaurant_id = request.form['restaurant_id']
        time = datetime.now()
        evaluation = request.form['evaluation']
        Food.create(user=user_id, restaurant=restaurant_id, time=time,evaluation=evaluation)
        return redirect(url_for('food.list'))
    
    users = User.select()
    restaurants = Restaurant.select()
    return render_template('food_add.html', users=users, restaurants=restaurants)

@food_bp.route("/edit/<int:food_id>", methods=["GET", "POST"])
def edit(food_id):
    pass

