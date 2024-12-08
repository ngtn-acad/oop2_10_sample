from flask import Blueprint, render_template, request, redirect, url_for
from models.jibyou import Jibyou
from models.user import User

jibyou_bp = Blueprint('jibyou', __name__, url_prefix='/jibyou')

@jibyou_bp.route('/')
def list():
    conditions = Jibyou.select()
    return render_template('jibyou_list.html', title='持病一覧', items=conditions)

@jibyou_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        condition = request.form.get('condition', '')
        check = 'check' in request.form
        
        Jibyou.create(
            user=user_id,
            condition=condition,
            check=check
        )
        return redirect(url_for('jibyou.list'))
    
    users = User.select()
    return render_template('jibyou_add.html', users=users)

@jibyou_bp.route('/edit/<int:jibyou_id>', methods=['GET', 'POST'])
def edit(jibyou_id):
    condition = Jibyou.get_or_none(Jibyou.id == jibyou_id)
    if not condition:
        return redirect(url_for('jibyou.list'))

    if request.method == 'POST':
        condition.user = request.form['user_id']
        condition.condition = request.form.get('condition', '')
        condition.check = 'check' in request.form
        condition.save()
        return redirect(url_for('jibyou.list'))

    users = User.select()
    return render_template('jibyou_edit.html', condition=condition, users=users)
