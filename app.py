from flask import Flask, render_template, jsonify
from models import initialize_database
from routes import blueprints
from peewee import fn
from models import Score

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
  
    # トップ5の得点を取得
    top_scores = (
        Score
        .select(Score.song, Score.challenger, fn.MAX(Score.score))
        .order_by(fn.MAX(Score.score).desc())
        .limit(5)
    )

    top_score_songs = []

    # データの整形
    for s in top_scores:
        temp = [s.challenger.name, s.song.song, s.score]
        top_score_songs.append(temp)

        
        
    # 曲の出現回数を集計し、上位5曲を取得
    top_songs = (
        Score
        .select(Score.song, fn.COUNT(Score.song).alias('count'))
        .group_by(Score.song)
        .order_by(fn.COUNT(Score.song).desc())
        .limit(5)
    )
    
    # データを整形
    song_names = [song.song.song for song in top_songs]  # 曲名
    song_counts = [song.count for song in top_songs]     # 出現回数
    
    # テンプレートにデータを渡してレンダリング
    return render_template("index.html", 
                           song_names=song_names, 
                           song_counts=song_counts,
                           top_score_songs=top_score_songs,
                          )
  

if __name__ == '__main__':
    app.run(port=8080, debug=True)