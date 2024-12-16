import math
from flask import Flask, render_template
from models import initialize_database,Status
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
    # Statusデータベースを全て取得、格納
    sList = []
    for i in range(len(Status)):
        sList.append(Status.get(Status.id == i+1))

    # キャラの使用率の取得、送信
    chara_unique = set([chara for chara in [st.name.name for st in sList]]) # キャラ名の一意のリスト(被りがない)
    chara_using = [chara for chara in [st.name.name for st in sList]] # 使用キャラのリスト(実際に使われてるキャラ)
    chara_usagerate = [math.floor(chara_using.count(chara)/len(sList)*100) for chara in chara_unique] # キャラごとの使用率
    # リストの結合、ソート
    chara_pair = list(zip(chara_unique,chara_usagerate))
    chara_unique_sorted, chara_usagerate_sorted = zip(*sorted(chara_pair))
    chara_use_data = {
        "type":'doughnut',
        "data": {
            "labels": [name for name in chara_unique_sorted], # 武器の名前
            "datasets": [
                {
                    "label": "使用率",
                    "data": chara_usagerate_sorted,  # 武器の使用率
                }
            ]
        },
        "options": {
            "plugins": {
                "title": {
                    "display": "true",
                    "text": '冒険者の人気度',
                    "font": {
                        "size": 30
                    }
                }
            }
        }
    }
    return render_template('index.html', chara_use_data=chara_use_data)

if __name__ == '__main__':
    app.run(port=8800,debug=True)