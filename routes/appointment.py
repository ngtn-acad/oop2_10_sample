from flask import Blueprint, render_template, request, redirect, url_for
from models.appointment import Appointment
from models.user import User
from datetime import datetime

appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointments')

@appointment_bp.route('/')
def list():
    appointments = (Appointment
                   .select()
                   .join(User)
                   .order_by(Appointment.appointment_datetime))
    
    for appointment in appointments:
        if isinstance(appointment.appointment_datetime, str):
            appointment.appointment_datetime = datetime.strptime(appointment.appointment_datetime, '%Y-%m-%dT%H:%M')
    return render_template('appointment_list.html', title='予約一覧', items=appointments)

@appointment_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        Appointment.create(
            user=request.form['user_id'],
            appointment_datetime=request.form['appointment_datetime'],
            department=request.form['department']
        )
        return redirect(url_for('appointment.list'))

    users = User.select()
    return render_template('appointment_add.html', users=users)

@appointment_bp.route('/edit/<int:appointment_id>', methods=['GET', 'POST'])
def edit(appointment_id):
    appointment = Appointment.get_or_none(Appointment.id == appointment_id)
    if not appointment:
        return redirect(url_for('appointment.list'))

    if request.method == 'POST':
        appointment.user = request.form['user_id']
        appointment.appointment_datetime = request.form['appointment_datetime']
        appointment.department = request.form['department']
        appointment.save()
        return redirect(url_for('appointment.list'))

    users = User.select()
    return render_template('appointment_edit.html', appointment=appointment, users=users)
