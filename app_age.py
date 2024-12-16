from flask import Flask, render_template
from peewee import fn, Case
from models import initialize_database, Score

app = Flask(__name__)

# データベースの初期化
initialize_database()

# ホームページのルート
@app.route('/')
def index():
    # 年代をカテゴリ
    age_group = Case(
        None,
        (
            (Score.age <= 10, "10代以下"),
            ((Score.age >= 11) & (Score.age <= 20), "20代"),
            ((Score.age >= 21) & (Score.age <= 30), "30代"),
            ((Score.age >= 31) & (Score.age <= 40), "40代"),
        ),
        "50代以上"
    )

    # 年代グループの出現回数を集計
    age_counts = (
        Score
        .select(age_group.alias('age_group'), fn.COUNT(Score.id).alias('count'))
        .group_by(age_group)
        .order_by(fn.COUNT(Score.id).desc())
    )

    # データを整形
    age_labels = [entry.age_group for entry in age_counts]  # 年代グループ
    counts = [entry.count for entry in age_counts]          # 出現回数

    # テンプレートにデータを渡してレンダリング
    return render_template("index.html", 
                           age_labels=age_labels, 
                           counts=counts)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
