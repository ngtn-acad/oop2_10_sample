from flask import Blueprint, render_template, request, redirect, url_for
from models.reservation import Reservation

# Blueprintの作成
reservation_bp = Blueprint('reservation', __name__, url_prefix='/reservations')


@reservation_bp.route('/')
def list():
    
    # データ取得
    reservations = Reservation.select()

    return render_template('reservation_list.html', title='予約リスト', items=reservations)