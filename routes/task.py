from flask import Blueprint, render_template, request, redirect, url_for
from models import Task, User

# Blueprintの作成
task_bp = Blueprint('task', __name__, url_prefix='/tasks')


@task_bp.route('/')
def list():
    tasks = Task.select()
    return render_template('task_list.html', title='業務記録', items=tasks)

@task_bp.route('/add', methods=['GET', 'POST'])
def add():

    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        user_id = request.form['user_id']
        type = request.form['type']
        content = request.form['content']
        Task.create(user=user_id, type=type, content=content)
        return redirect(url_for('task.list'))
    
    return render_template('task_add.html')


@task_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.get_or_none(Task.id == task_id)
    if not task:
        return redirect(url_for('task.list'))

    if request.method == 'POST':
        task.user = request.form['user_id']
        task.type = request.form['type']
        task.content = request.form['content']
        task.save()
        return redirect(url_for('task.list'))

    return render_template('task_edit.html', task=task)