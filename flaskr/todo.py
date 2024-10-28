from flask import Blueprint, render_template, session, request, redirect, flash
from .auth import is_logged_in
from flaskr.utils.token import decode_token
from flaskr.models.todo import Todo
import json


bp = Blueprint("todo", __name__, url_prefix="/todo", template_folder="templates/todo")
file_path = "flaskr/data/todo.json"


@bp.route("/add", methods=["GET", "POST"])
@is_logged_in
def add():
    if request.method == "POST":
        title = request.form["title"]
        user_id = decode_token(session["token"]).get("id")
        todo = Todo(user_id, title)
        with open(file_path, "r") as todo_file:
            try:
                data = json.load(todo_file)
            except json.JSONDecodeError:
                data = {}
        if "todos" not in data:
            data["todos"] = []
        data["todos"].append(todo.__dict__)
        with open(file_path, "w") as todo_file:
            json.dump(data, todo_file, indent=4)
            flash("Todo added successfully", "success")
            return redirect("/")
    else:
        return render_template("todo.html", mode="add")


@bp.route("/edit/<string:id>", methods=["GET", "POST"])
@is_logged_in
def edit(id):
    user_id = decode_token(session["token"]).get("id")
    with open(file_path, "r") as todo_file:
        try:
            data = json.load(todo_file)
        except json.JSONDecodeError:
            data = {}
        if "todos" not in data:
            data["todos"] = []

    if request.method == "POST":
        for todo in data["todos"]:
            if todo["id"] == id:
                if todo["user_id"] != user_id:
                    flash("You are not allowed to edit this todo", "danger")
                    return redirect("/")
                todo["title"] = request.form["title"]
                todo["completed"] = False
                with open(file_path, "w") as todo_file:
                    json.dump(data, todo_file, indent=4)
                    flash("Todo updated successfully", "success")
                    return redirect("/")
    else:
        for todo in data["todos"]:
            if todo["id"] == id:
                if todo["user_id"] != user_id:
                    flash("You are not allowed to edit this todo", "danger")
                    return redirect("/")
                return render_template(
                    "todo.html", mode="edit", id=id, title=todo["title"]
                )


@bp.route("/complete/<string:id>", methods=["GET"])
@is_logged_in
def complete(id):
    with open(file_path, "r") as todo_file:
        try:
            data = json.load(todo_file)
        except json.JSONDecodeError:
            data = {}
    if "todos" not in data:
        flash("Todo not found", "danger")
        return redirect("/")
    user_id = decode_token(session["token"]).get("id")
    for todo in data["todos"]:
        if todo["id"] == id:
            if todo["user_id"] != user_id:
                flash("You are not allowed to complete this todo", "danger")
                return redirect("/")
            todo["completed"] = True
            with open(file_path, "w") as todo_file:
                json.dump(data, todo_file, indent=4)
                flash("Todo completed successfully", "success")
                return redirect("/")
    flash("Todo not found", "danger")
    return redirect("/")

@bp.route("/delete/<string:id>", methods=["GET"])
@is_logged_in
def delete(id):
    with open(file_path, "r") as todo_file:
        try:
            data = json.load(todo_file)
        except json.JSONDecodeError:
            data = {}
    if "todos" not in data:
        flash("Todo not found", "danger")
        return redirect("/")
    user_id = decode_token(session["token"]).get("id")
    for todo in data["todos"]:
        if todo["id"] == id:
            if todo["user_id"] != user_id:
                flash("You are not allowed to delete this todo", "danger")
                return redirect("/")
            data["todos"].remove(todo)
            with open(file_path, "w") as todo_file:
                json.dump(data, todo_file, indent=4)
                flash("Todo deleted successfully", "success")
                return redirect("/")
    flash("Todo not found", "danger")
    return redirect("/")