from flask import Flask, render_template, redirect, request, Blueprint
from models.attendance import Attendance
from models.gym_class import Class

import repositories.classes_repository as classes_repository
import repositories.members_repository as members_repository
import repositories.attendances_repository as attendances_repository

classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    classes = classes_repository.select_all()
    return render_template("/classes/view.html", title="View classes", all_classes=classes)

@classes_blueprint.route("/classes/<id>/edit")
def edit_class(id):
    gym_class = classes_repository.select(id)
    return render_template("/classes/edit.html", title="Edit class",gym_class=gym_class)

@classes_blueprint.route("/classes/<id>/edit", methods=["POST"])
def update_class(id):
    name = request.form["name"]
    type = request.form["type"]
    date = request.form["date"]
    time = request.form["time"]
    gym_class = Class(name, type, date, time, id)
    classes_repository.update(gym_class)
    return redirect("/classes")

@classes_blueprint.route("/classes/new")
def add_class():
    return render_template("/classes/new.html", title="Add new class")

@classes_blueprint.route("/classes/new", methods=["POST"])
def create_class():
    name = request.form["name"]
    type = request.form["type"]
    date = request.form["date"]
    time = request.form["time"]
    gym_class = Class(name, type, date, time)
    classes_repository.save(gym_class)
    return redirect("/classes")

@classes_blueprint.route("/classes/<id>/view")
def booked_members(id):
    members = []
    members = classes_repository.members(id)
    all_members = members_repository.select_all()
    gym_class = classes_repository.select(id)
    class_name = gym_class.name
    member_ids = classes_repository.member_ids(id)
    return render_template("/classes/booked_members.html", title="Booked members", gym_class=gym_class, class_name=class_name, booked_members=members, all_members=all_members, all_member_ids=member_ids, id=id)

@classes_blueprint.route("/classes/<id>/<class_id>/add_member")
def add_member_to_class(id, class_id):
    attendance = Attendance(id, class_id)
    attendances_repository.save(attendance)
    return redirect("/classes")