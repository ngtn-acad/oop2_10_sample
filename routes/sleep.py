from flask import Blueprint, render_template, request, redirect, url_for,Response 
import json
from models import Sleep, User


# Blueprintの作成
sleep_bp = Blueprint('sleep', __name__, url_prefix='/sleeps')


@sleep_bp.route('/')
def list():
    
    # データ取得
    sleeps = Sleep.select()

    return render_template('sleep_list.html', title='睡眠', items=sleeps)

# @sleep_bp.route('/data')
# def sleep_data():
#     sleeps = Sleep.select()
#     sleep_data = [{'user': sleep.user.name, 'start': sleep.start, 'end': sleep.end} for sleep in sleeps]
#     return Response(json.dumps(sleep_data), mimetype='application/json')


@sleep_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        user_id = request.form['user_id']
        start = request.form['start']
        end = request.form['end']
        Sleep.create(user_id=user_id, start = start, end = end)
        return redirect(url_for('sleep.list'))
    
    users = User.select()
    return render_template('sleep_add.html',users=users)


@sleep_bp.route('/edit/<int:sleep_id>', methods=['GET', 'POST'])
def edit(sleep_id):
    sleep = Sleep.get_or_none(Sleep.id == sleep_id)
    if not sleep:
        return redirect(url_for('sleep.list'))

    if request.method == 'POST':
        sleep.user = request.form['user_id']
        sleep.start = request.form['start']
        sleep.end = request.form['end']
        sleep.save()
        return redirect(url_for('sleep.list'))
    
    return render_template('sleep_edit.html', sleep=sleep, users=User.select())
