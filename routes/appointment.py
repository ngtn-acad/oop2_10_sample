from flask import Blueprint, render_template, request, redirect, url_for
from models import Appointment
from datetime import datetime

appointment_bp = Blueprint('appointment', __name__, url_prefix='/appointments')

@appointment_bp.route('/')
def list():
    appointments = Appointment.select().order_by(Appointment.appointment_datetime)
    return render_template('appointment_list.html', title='予約一覧', items=appointments)

@appointment_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        appointment_datetime = datetime.strptime(f"{date} {time}", '%Y-%m-%d %H:%M')
        
        Appointment.create(
            appointment_datetime=appointment_datetime,
            patient_name=request.form['patient_name']
        )
        return redirect(url_for('appointment.list'))
    
    return render_template('appointment_add.html')

@appointment_bp.route('/edit/<int:appointment_id>', methods=['GET', 'POST'])
def edit(appointment_id):
    appointment = Appointment.get_or_none(Appointment.id == appointment_id)
    if not appointment:
        return redirect(url_for('appointment.list'))

    if request.method == 'POST':
        date = request.form['date']
        time = request.form['time']
        appointment_datetime = datetime.strptime(f"{date} {time}", '%Y-%m-%d %H:%M')
        
        appointment.appointment_datetime = appointment_datetime
        appointment.patient_name = request.form['patient_name']
        appointment.save()
        return redirect(url_for('appointment.list'))

    return render_template('appointment_edit.html', appointment=appointment)
