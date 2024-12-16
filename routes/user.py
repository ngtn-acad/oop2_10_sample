from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models import User
import matplotlib
matplotlib.use("Agg")  # GUIバックエンドを無効化
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter
# Blueprintの作成
user_bp = Blueprint('user', __name__, url_prefix='/users')


@user_bp.route('/')
def list():
    
    # データ取得
    users = User.select()

    return render_template('user_list.html', title='ユーザー一覧', items=users)


@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        contact = request.form['contact']
        User.create(name=name, age=age, contact=contact)
        return redirect(url_for('user.list'))
    
    return render_template('user_add.html')


@user_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = User.get_or_none(User.id == user_id)
    if not user:
        return redirect(url_for('user.list'))
    
    if request.method == 'POST':
        user.name = request.form['name']
        user.age = request.form['age']
        user.contact = request.form['contact']
        user.save()
        return redirect(url_for('user.list'))
    
    return render_template('user_edit.html', user=user)

@user_bp.route('/graph')
def index():
    # 年齢データを取得
    ages = [user.age for user in User.select()]

    # 年齢を10代ごとに区分
    bins = range(0, 101, 10)
    age_groups = [(age // 10) * 10 for age in ages]

    # 年齢分布を集計
    age_counts = Counter(age_groups)

    # ラベルと値を生成
    labels = [f"{start}~{start+9}" for start in bins[:-1]]
    counts = [age_counts.get(start, 0) for start in bins[:-1]]

    # グラフの作成
    plt.figure()
    plt.bar(labels, counts, color="skyblue", edgecolor="black")
    plt.xlabel("Age")
    plt.ylabel("People")
    plt.title("Age distribution")
    plt.ylim(0, 10)
    plt.tight_layout()

    # グラフをBase64形式でエンコード
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    base64_img = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Base64画像をHTMLに埋め込む
    graph_html = f'<img src="data:image/png;base64,{base64_img}" alt="Graph">'
    return render_template("graph.html", graph=graph_html)