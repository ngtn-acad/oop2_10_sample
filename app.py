from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.most_eaten_ranking import most_eaten_ranking

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
   
    return render_template('index.html' , foods = most_eaten_ranking() )

if __name__ == '__main__':
    app.run(port=8080, debug=True)
