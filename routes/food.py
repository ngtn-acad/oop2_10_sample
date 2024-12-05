from flask import Blueprint, render_template, request, redirect, url_for
from models.food import Food

# Blueprintの作成
food_bp = Blueprint('food', __name__, url_prefix='/foods')


@food_bp.route('/')
def list():
    
    # データ取得
    foods = Food.select()

    return render_template('food_list.html', title='フードメニュー', items=foods)