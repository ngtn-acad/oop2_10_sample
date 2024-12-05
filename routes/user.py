from flask import Blueprint, render_template, request, redirect, url_for
from models import User

# Blueprintの作成
user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/")
def list():

    # データ取得
    users = User.select()

    return render_template("user_list.html", title="ユーザー一覧", items=users)


@user_bp.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
        student_id = request.form["student_id"]
        name = request.form["name"]
        gender = request.form["gender"]
        age = request.form["age"]

        User.create(student_id=student_id, name=name, gender=gender, age=age)

        return redirect(url_for("user.list"))

    return render_template("user_add.html")


@user_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit(user_id):
    user = User.get_or_none(User.id == user_id)
    if not user:
        return redirect(url_for("user.list"))

    if request.method == "POST":
        user.student_id = request.form["student_id"]
        user.name = request.form["name"]
        user.gender = request.form["gender"]
        user.age = request.form["age"]

        user.save()

        return redirect(url_for("user.list"))

    return render_template("user_edit.html", user=user)
