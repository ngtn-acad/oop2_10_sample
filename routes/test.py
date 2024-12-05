from flask import Blueprint, render_template, request, redirect, url_for
from models import Test, User, Product  # Test、User、Product モデルをインポート
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

        print(f"Received test_id: {test_id}")  # 送信されたtest_idをログに出力


        # Productテーブルから指定されたtest_idの教科を取得
        selected_test = Product.get(Product.id == test_id)
        print(f"Selected test: {selected_test.name}")  # 選択された教科をログに出力
        
        # Testデータの作成
        test = Test.create(user_id=user_id, name=selected_test.name, score=score)

        return redirect(url_for('test.list'))  # テストデータ一覧ページにリダイレクト

    users = User.select()  # ユーザーリストを取得
    return render_template('test_add.html', users=users)