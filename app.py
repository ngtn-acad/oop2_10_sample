from flask import Flask, render_template
from peewee import fn
from models import initialize_database, Challenger
from routes import blueprints

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    # 年代別の人数を取得
    age_list = (
        Challenger
        .select(Challenger.age, fn.COUNT(Challenger.id).alias('count'))
        .group_by(Challenger.age)
    )

    # 年代ラベル
    age_labels = ['10代以下', '20代', '30代', '40代', '50代以上']
    
    # 初期化された年代別カウント
    age_counts = [0, 0, 0, 0, 0]

    # 年代ごとに人数をカウント
    for al in age_list:
        if al.age <= 19:
            age_counts[0] += al.count
        elif al.age <= 29:
            age_counts[1] += al.count
        elif al.age <= 39:
            age_counts[2] += al.count
        elif al.age <= 49:
            age_counts[3] += al.count
        else:
            age_counts[4] += al.count

    # データを整形してテンプレートに渡す
    return render_template('index.html', age_labels=age_labels, age_counts=age_counts)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
