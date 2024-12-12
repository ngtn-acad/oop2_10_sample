from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
from routes.most_eaten_ranking import most_eaten_ranking



app = Flask(__name__)

# データベースの初期化
initialize_database()

# print(most_eaten_ranking())

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    # foods = [
    #     {
    #         "food":"a",
    #     "restaurant":"b",
    #     "eaten_num":10
    #     },
    #     {
    #         "food":"c",
    #     "restaurant":"d",
    #     "eaten_num":20
    #     },
    #     {
    #         "food":"e",
    #     "restaurant":"f",
    #     "eaten_num":30
    #     },
    #             {
    #         "food":"g",
    #     "restaurant":"h",
    #     "eaten_num":40
    #     },
    #             {
    #         "food":"i",
    #     "restaurant":"j",
    #     "eaten_num":50
    #     }
    #     ]
    return render_template('index.html' , foods = most_eaten_ranking() )

if __name__ == '__main__':
    app.run(port=8080, debug=True)
