from flask import Blueprint, render_template, request, redirect, url_for
from models.drink import Drink

# Blueprintの作成
drink_bp = Blueprint('drink', __name__, url_prefix='/drinks')


@drink_bp.route('/')
def list():
    
    # データ取得
    drinks = Drink.select()

    return render_template('drink_list.html', title='ドリンクメニュー', items=drinks)