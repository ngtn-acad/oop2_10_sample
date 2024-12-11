from flask import Blueprint, render_template, request, redirect, url_for
from models import Test, User # Test、User、Product モデルをインポート
from peewee import DoesNotExist

test_bp = Blueprint('test', __name__, url_prefix='/test')

@test_bp.route('/')
def list():
    # テストデータを取得（最新のデータも含めて表示）
    tests = Test.select()
    return render_template('test_list.html', title='テストデータ一覧', items=tests)

@test_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id']  # ユーザーID
        test_id = request.form['test_id']  # 教科ID
        score = request.form['score']  # 点数
        """
        print(f"Received test_id: {test_id}")  # 送信されたtest_idをログに出力


        # Productテーブルから指定されたtest_idの教科を取得
        selected_test = Test.get_or_none(Test.id == test_id)
        if not selected_test.name:
            return redirect(url_for('test.list'))
        print(f"Selected test: {selected_test.name}")  # 選択された教科をログに出力
        """
        # Testデータの作成
        Test.create(user_id=user_id, name=test_id, score=score)
        return redirect(url_for('test.list'))  # テストデータ一覧ページにリダイレクト

    users = User.select()  # ユーザーリストを取得
    return render_template('test_add.html', users=users)

@test_bp.route('/edit/<int:test_id>', methods=['GET', 'POST'])
def edit(test_id):
    test = Test.get_or_none(Test.id == test_id)
    if not test:
        return redirect(url_for('test.list'))

    if request.method == 'POST':
        test.user = request.form['user_id']
        test.name = request.form['test_id']
        test.score = request.form['score']
        test.save()
        return redirect(url_for('test.list'))

    return render_template('test_edit.html', test=test, users=User.select())