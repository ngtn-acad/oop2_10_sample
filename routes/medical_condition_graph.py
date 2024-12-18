import matplotlib.pyplot as plt 
from flask import Flask,Blueprint, render_template
import io
import base64
import numpy as np
from models import MedicalCondition


medical_graph_bp = Blueprint('medical_graph_bp', __name__, url_prefix='/')

@medical_graph_bp.route("/")
def index():
    fever = 0
    vomiting = 0
    headache = 0
    dizziness = 0
    other = 0
    

    fever_medical = [user.fever for user in MedicalCondition.select()]
    for fever_user in fever_medical:
        if(fever_user):
            print("fever",fever_user)
            fever += 1

    vomiting_medical = [user.vomiting for user in MedicalCondition.select()]
    for vomiting_user in vomiting_medical:
        if(vomiting_user):
            vomiting += 1

    headache_medical = [user.headache for user in MedicalCondition.select()]
    for headache_user in headache_medical:
        if(headache_user):
            headache += 1

    dizziness_medical = [user.dizziness for user in MedicalCondition.select()]
    for dizziness_user in dizziness_medical:
        if(dizziness_user):
            dizziness += 1

    other_medical = [user.other for user in MedicalCondition.select()]
    for other_user in other_medical:
        if(other_user):
            other += 1
    
    print("fever",type(fever))


    # 棒グラフ
    m = ("1", "2", "3", "4", "5")
    y_pos = np.arange(len(m))
    # 下記sales変数内の数値を変更して、色々実行してみてください。
    sales = [fever ,vomiting ,headache,dizziness,other]

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
