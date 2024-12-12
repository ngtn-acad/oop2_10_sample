from flask import Blueprint, render_template, request, redirect, url_for,Response
import json
from models import Test, User # Test、User、Product モデルをインポート
from peewee import DoesNotExist

test_bp = Blueprint('test', __name__, url_prefix='/test')

@test_bp.route('/')
def list():
    # テストデータを取得（最新のデータも含めて表示）
    tests = Test.select()
    return render_template('test_list.html', title='テストデータ一覧', items=tests)

# @test_bp.route('/data')
# def test_data():
#     tests = Test.select()
#     test_data = [{'user': test.user.name, 'score': test.japanese + test.math + test.english} for test in tests]
#     return Response(json.dumps(test_data), mimetype='application/json')

@test_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user_id'] 
        # ユーザーID
        
        #国語の点数        
        japanese = request.form['japanese']  # 日本語の点数
        math = request.form['math']
        english = request.form['english']
        # Testデータの作成
        Test.create(user_id=user_id, japanese=japanese, math=math , english=english)
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
        test.japanese = request.form['japanese']
        test.math = request.form['math']
        test.english = request.form['english']
        test.save()
        return redirect(url_for('test.list'))

    return render_template('test_edit.html', test=test, users=User.select())