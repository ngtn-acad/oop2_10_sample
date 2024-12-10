from flask import Blueprint, render_template, request, redirect, url_for
from models import Task, User

# Blueprintの作成
task_bp = Blueprint('task', __name__, url_prefix='/tasks')


@task_bp.route('/')
def list():
    tasks = Task.select()
    return render_template('task_list.html', title='業務記録', items=tasks)


# @task_bp.route('/task/add')
# def add():
#     User = User.select()
#     return render_template('task_add.html', title='業務追加', items=User)

@task_bp.route('/add', methods=['GET', 'POST'])
def add():

    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        user_id = request.form['user_id']
        task_name = request.form['task_name']
        task_content = request.form['task_content']
        Task.create(user_id=user_id, task_name=task_name, task_content=task_content)
        return redirect(url_for('task.list'))
    
    users = User.select()
    return render_template('task_add.html', users=users)


@task_bp.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.get_or_none(Task.id == task_id)
    if not task:
        return redirect(url_for('task.list'))

    if request.method == 'POST':
        task.user_id = request.form['user_id']
        task.task_name = request.form['task_name']
        task.task_content = request.form['task_content']
        task.save()
        return redirect(url_for('task.list'))

    users = User.select()
    return render_template('task_edit.html', task=task, users=users)