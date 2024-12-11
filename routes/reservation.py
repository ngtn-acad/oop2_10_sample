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

  
#フード商品の編集
@food_bp.route('/edit/<int:food_number>', methods=['GET', 'POST'])
def edit(food_number):
    food_numer = Food_number.get_or_none(Food_number.id == food_number)
    if not food_number:
        return redirect(url_for('food_number.list'))

    if request.method == 'POST':
        food_numer.name = request.form['name']
        food_number.price = request.form['price']
        food_number.save()
        return redirect(url_for('food_number.list'))

    return render_template('food_number_edit.html', food_number=food_number)



#ドリンク商品の編集
@drink_bp.route('/edit/<int:drink_number>', methods=['GET', 'POST'])
def edit(drink_number):
    drink_number = Drink_number.get_or_none(Drinnk_number.id == drink_number)
    if not drink_number:
        return redirect(url_for('drink_number.list'))

    if request.method == 'POST':
        drink_number.name = request.form['name']
        drink_number.price = request.form['price']
        drink_number.save()
        return redirect(url_for('drink_number.list'))

    return render_template('drink_number_edit.html', drink_number=drink_number)


#顧客名の編集
@customer_bp.route('/edit/<int:customer_id',methods=['GET','POST'])
def edit(customer_id):
     customer = Customer.get_or_none(Customer.id == customer_id)
     if not customer:
        return redirect(url_for('customer.list'))

     if request.method == 'POST':
        customer.name = request.form['name']
        customer.numPeople = request.form['numPeople']
        customer.save()
        return redirect(url_for('customer.list'))

     return render_template('customer_edit.html', customer=customer)     
  