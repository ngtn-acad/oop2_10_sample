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
        food_name = request.form['food_name']
        restaurant_id = request.form['restaurant_id']
        time = datetime.now()
        evaluation = request.form['evaluation']
        Food.create(user=user_id, food=food_name,restaurant=restaurant_id, time=time,evaluation=evaluation)
        return redirect(url_for('food.list'))
    
    users = User.select()
    restaurants = Restaurant.select()
    return render_template('food_add.html', users=users, restaurants=restaurants)

@food_bp.route("/edit/<int:food_id>", methods=["GET", "POST"])
def edit(food_id):
    food = Food.get_or_none(Food.id == food_id)
    if not food:
        return redirect(url_for("food.list"))
    
    if request.method == "POST":
        food.user = request.form["user_id"]
        food.food = request.form["food_name"]
        food.restaurant = request.form["restaurant_id"]
        food.time = datetime.now()
        food.evaluation = request.form["evaluation"]
        
        food.save()
        
        return redirect(url_for("food.list"))
    
    return render_template("food_edit.html", food=food, users=User.select(), restaurants=Restaurant.select())
