from flask import Blueprint, render_template, request, redirect, url_for
from models import Goods

# Blueprintの作成
goods_bp = Blueprint("goods", __name__, url_prefix="/goods")


@goods_bp.route("/")
def list():
    goods = Goods.select()
    return render_template("goods_list.html", title="商品一覧", items=goods)


@goods_bp.route("/add", methods=["GET", "POST"])
def add():

    # POSTで送られてきたデータは登録
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        categori = request.form["categori"]
        Goods.create(name=name, price=price, categori=categori)
        return redirect(url_for("goods.list"))

    return render_template("goods_add.html")


@goods_bp.route("/edit/<int:goods_id>", methods=["GET", "POST"])
def edit(goods_id):
    good = Goods.get_or_none(Goods.id == goods_id)
    if not good:
        return redirect(url_for("goods.list"))

    if request.method == "POST":
        good.name = request.form["name"]
        good.price = request.form["price"]
        categori = request.form["categori"]
        good.save()
        return redirect(url_for("goods.list"))

    return render_template("goods_edit.html", goods=good)
