import matplotlib.pyplot as plt 
from flask import Flask,Blueprint, render_template
import io
import base64
import numpy as np

medical_graph_bp = Blueprint('medical_graph_bp', __name__, url_prefix='/')

@medical_graph_bp.route("/")
def index():

    # # グラフを作成    
    # a = range(0, 7)
    # b = [55,21,61,98,85,52,99]
    # plt.bar(a, b)
    # # plt.barh(a, b) # 横棒の棒グラフ
    # plt.show()


    

    # 棒グラフ
    m = ("1", "2", "3", "4", "5", "6", "7","8","9","10","11","12")
    y_pos = np.arange(len(m))
    # 下記sales変数内の数値を変更して、色々実行してみてください。
    sales = [10 ,18 ,32,54,65,96, 120, 140, 145,162, 188, 202]

    plt.bar(y_pos, sales, alpha=0.5)
    plt.ylabel("Usage")
    plt.title("Sales Trends") # 売上推移

    # グラフをBase64形式でエンコード    
    buf = io.BytesIO()    
    plt.savefig(buf, format="png")
    buf.seek(0)
    base64_img = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Base64画像をHTMLに埋め込む
    graph_html = f'<img src="data:image/png;base64,{base64_img}" alt="Graph">'

    # HTMLにグラフデータを渡す
    return render_template("index.html", graph = graph_html)
