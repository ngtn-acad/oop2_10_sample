from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.graphs import fetch_sleep_test_data, create_graph


import plotly.graph_objects as go

# from routes.sleep import sleep_bp
# from routes.test import test_bp
# from routes.graph import graph_bp


app = Flask(__name__)


# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

fetch_sleep_test_data()
create_graph()

# ホームページのルート
@app.route('/')
def index():
    graph = create_graph()
    return render_template('index.html', graph = graph)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
