from flask import Blueprint, render_template, request, redirect, url_for
from models.medical_condition import MedicalCondition
from models.user import User

medical_condition_bp = Blueprint('medical_condition', __name__, url_prefix='/medical-conditions')

@medical_condition_bp.route('/')
def list():
    conditions = MedicalCondition.select()
    return render_template('medical_condition_list.html', title='症状一覧', items=conditions)

@medical_condition_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        conditions = request.form.getlist('condition')
        for condition in conditions:
            MedicalCondition.create(
                user=user_id,
                condition=condition
            )
        return redirect(url_for('medical_condition.list'))

    users = User.select()
    return render_template('medical_condition_add.html', users=users)

@medical_condition_bp.route('/edit/<int:condition_id>', methods=['GET', 'POST'])
def edit(condition_id):
    condition = MedicalCondition.get_or_none(MedicalCondition.id == condition_id)
    if not condition:
        return redirect(url_for('medical_condition.list'))

    if request.method == 'POST':
        condition.user = request.form['user_id']
        condition.condition = request.form['condition']
        condition.save()
        return redirect(url_for('medical_condition.list'))

    users = User.select() 
    return render_template('medical_condition_edit.html', condition=condition, users=users) 
