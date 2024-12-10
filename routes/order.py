from flask import Blueprint, render_template, request, redirect, url_for
from models import Order, Customer, Goods
from datetime import datetime

# Blueprintの作成
order_bp = Blueprint("order", __name__, url_prefix="/orders")


@order_bp.route("/")
def list():
    orders = Order.select()
    return render_template("order_list.html", title="注文一覧", items=orders)


@order_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        customer_id = request.form["customer_id"]
        goods_id = request.form["goods_id"]
        order_date = datetime.now()
        Order.create(customer=customer_id, goods=goods_id, order_date=order_date)
        return redirect(url_for("order.list"))

    customers = Customer.select()
    goods = Goods.select()
    return render_template("order_add.html", customers=customers, goods=goods)


@order_bp.route("/edit/<int:order_id>", methods=["GET", "POST"])
def edit(order_id):
    order = Order.get_or_none(Order.id == order_id)
    if not order:
        return redirect(url_for("order.list"))

    if request.method == "POST":
        order.customer = request.form["customer_id"]
        order.good = request.form["good_id"]
        order.save()
        return redirect(url_for("order.list"))

    customers = Customer.select()
    goods = Goods.select()
    return render_template(
        "order_edit.html", order=order, customers=customers, goods=goods
    )
