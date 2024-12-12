from flask import Flask, render_template
from models import initialize_database
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
    # ダミーデータ
    data = {
        "labels": ["9:00", "10:00", "11:00", "12:00", "13:00"],  # 時間
        "datasets": [
            {
                "label": "Temperature (°C)",
                "data": [20, 22, 24, 23, 21],  # 温度
            }
        ]
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)