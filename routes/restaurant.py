from flask import Blueprint, render_template, request, redirect, url_for
from models import Restaurant

# Blueprintの作成
restaurant_bp = Blueprint("restaurant", __name__, url_prefix="/restaurants")


@restaurant_bp.route("/")
def list():

    # データ取得
    restaurants = Restaurant.select()
    return render_template("restaurant_list.html", title="お店一覧", items=restaurants)


@restaurant_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]
        Restaurant.create(name=name, address=address)
        return redirect(url_for("restaurant.list"))

    return render_template("restaurant_add.html")


@restaurant_bp.route("/edit/<int:restaurant_id>", methods=["GET", "POST"])
def edit(restaurant_id):
    restaurant = Restaurant.get_or_none(Restaurant.id == restaurant_id)
    if not restaurant:
        return redirect(url_for("restaurant.list"))

    if request.method == "POST":
        restaurant.name = request.form["name"]
        restaurant.address = request.form["address"]
        restaurant.save()
        return redirect(url_for("restaurant.list"))

    return render_template("restaurant_edit.html", restaurant=restaurant)
