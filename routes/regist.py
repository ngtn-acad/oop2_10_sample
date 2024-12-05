from flask import Blueprint, render_template, request, redirect, url_for
from models import Regist, User, Subject
from datetime import datetime

# Blueprintの作成
regist_bp = Blueprint('regist', __name__, url_prefix='/regist')


@regist_bp.route('/')
def list():
    regist = Regist.select()
    return render_template('regist_list.html', title='履修リスト', regists=regist)


@regist_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']
        subject_id = request.form['subject_id']
        regist_date = datetime.now()
        Regist.create(user=user_id, subject=subject_id, regist_date=regist_date)
        return redirect(url_for('regist.list'))
    
    users = User.select()
    subjects = Subject.select()
    return render_template('regist_add.html', users=users, subjects=subjects)


@regist_bp.route('/edit/<int:regist_id>', methods=['GET', 'POST'])
def edit(regist_id):
    regist = Regist.get_or_none(Regist.id == regist_id)
    if not regist:
        return redirect(url_for('regist.list'))

    if request.method == 'POST':
        regist.user = request.form['user_id']
        regist.subject = request.form['subject_id']
        regist.save()
        return redirect(url_for('regist.list'))

    users = User.select()
    subjects = Subject.select()
    return render_template('regist_edit.html', regist=regist, users=users, subjects=subjects)
