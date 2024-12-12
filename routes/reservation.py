from flask import Blueprint, render_template, request, redirect, url_for
from models.reservation import Reservation

# Blueprintの作成
reservation_bp = Blueprint('reservation', __name__, url_prefix='/reservations')
food_bp = Blueprint('food', __name__, url_prefix='/food')
drink_bp = Blueprint('drink', __name__, url_prefix='/drink')
customer_bp = Blueprint('customer', __name__, url_prefix='/customer')


@reservation_bp.route('/')
def list():
    
    # データ取得
    reservations = Reservation.select()

    return render_template('reservation_list.html', title='予約リスト', items=reservations)

#予約の追加
@reservation_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        numpeople = request.form['numpeople']
        numfood = request.form['numfood']
        numdrink = request.form['numdrink']
        Reservation.create(numpeople=numpeople, numfood=numfood, numdrink=numdrink)
        return redirect(url_for('reservation_add.list'))
    
    return render_template('reservation_add.html')

#フード商品の編集
@reservation_bp.route('/edit', methods=['GET', 'POST'])
def edit(reservation_id):
    reservation = Reservation.get_or_none(Reservation.id == reservation_id)
    if not reservation:
        return redirect(url_for('reservation.list'))

    if request.method == 'POST':
        reservation.numpeople = request.form['numpeople']
        reservation.numfood = request.form['numfood']
        reservation.numdrink = request.form['numdrink']
        reservation.save()
        return redirect(url_for('reservation.list'))

    return render_template('reservation_edit.html', reservation=reservation)