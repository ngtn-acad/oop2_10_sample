from flask import Blueprint, render_template, request, redirect, url_for

booking_bp = Blueprint('booking', __name__, url_prefix='/booking')

@booking_bp.route('/request')
def request():
    return render_template('booking_request.html', title='予約申込') 