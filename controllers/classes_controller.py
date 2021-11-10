from flask import Flask, render_template, redirect, request, Blueprint
from models.attendance import Attendance
from models.gym_class import Class
from datetime import time, datetime

import repositories.classes_repository as classes_repository
import repositories.members_repository as members_repository
import repositories.attendances_repository as attendances_repository

import pdb

classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    classes = classes_repository.select_all()
    class_search = None
    return render_template("/classes/view.html", title="View classes", all_classes=classes, class_search=class_search)

@classes_blueprint.route("/classes/<id>/edit")
def edit_class(id):
    gym_class = classes_repository.select(id)
    return render_template("/classes/edit.html", title="Edit class",gym_class=gym_class)

@classes_blueprint.route("/classes/<id>/edit", methods=["POST"])
def update_class(id):
    name = request.form["name"]
    type = request.form["type"]
    date = request.form["date"]
    formatted_time = request.form["time"][0:5]
    time = datetime.strptime(formatted_time, "%H:%M").time()
    capacity = request.form["capacity"]
    gym_class = Class(name, type, date, time, capacity, id)
    classes_repository.update(gym_class)
    
    members = []
    members = classes_repository.members(id)
    all_members = members_repository.select_all()
    gym_class = classes_repository.select(id)
    class_name = gym_class.name
    member_ids = classes_repository.member_ids(id)
    number_attendees = len(members)

    return render_template("/classes/booked_members.html", title="Booked members", gym_class=gym_class, class_name=class_name, booked_members=members, all_members=all_members, all_member_ids=member_ids, number_attendees=number_attendees, id=id)

@classes_blueprint.route("/classes/new")
def add_class():
    return render_template("/classes/new.html", title="Add new class")

@classes_blueprint.route("/classes/new", methods=["POST"])
def create_class():
    name = request.form["name"]
    type = request.form["type"]
    date = request.form["date"]
    time = datetime.strptime(request.form["time"], "%H:%M").time()
    capacity = request.form["capacity"]
    gym_class = Class(name, type, date, time, capacity)
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
    number_attendees = len(members)
    member_name = None
    return render_template("/classes/booked_members.html", title="Booked members", gym_class=gym_class, class_name=class_name, booked_members=members, all_members=all_members, all_member_ids=member_ids, number_attendees=number_attendees, id=id, member_name=member_name)

# @classes_blueprint.route("/classes/<id>/<class_id>/add_member")
# def add_member_to_class(id, class_id):
#     attendance = Attendance(id, class_id)
#     attendances_repository.save(attendance)
#     return redirect("/classes")

##replaced with multi-select

@classes_blueprint.route("/classes/booked_members/<member_id>/<class_id>/remove")
def remove_member(member_id, class_id):
    classes_repository.member_remove(member_id, class_id)

    members = []
    members = classes_repository.members(class_id)
    all_members = members_repository.select_all()
    gym_class = classes_repository.select(class_id)
    class_name = gym_class.name
    member_ids = classes_repository.member_ids(class_id)
    number_attendees = len(members)
    member_name = None

    return render_template("/classes/booked_members.html", title="Booked members", gym_class=gym_class, class_name=class_name, booked_members=members, all_members=all_members, all_member_ids=member_ids, number_attendees=number_attendees, id=class_id, member_name=member_name)

@classes_blueprint.route("/classes/<class_id>/booked_members", methods=["POST"])
def add_multiple_members(class_id):
    members = []
    members = request.form.to_dict(flat=False)["member_id"]
    for row in members:
        attendance = Attendance(row, class_id)
        attendances_repository.save(attendance)
    
    members = []
    members = classes_repository.members(class_id)
    all_members = members_repository.select_all()
    gym_class = classes_repository.select(class_id)
    class_name = gym_class.name
    member_ids = classes_repository.member_ids(class_id)
    number_attendees = len(members)
    member_name = None

    return render_template("/classes/booked_members.html", title="Booked members", gym_class=gym_class, class_name=class_name, booked_members=members, all_members=all_members, all_member_ids=member_ids, number_attendees=number_attendees, id=class_id, member_name=member_name)

@classes_blueprint.route("/classes/<id>/delete")
def delete_of_class(id):
    attendances_repository.delete_class_in_attendances(id)
    classes_repository.delete_class(id)
    return redirect("/classes")

@classes_blueprint.route("/classes/<id>/member_search", methods=["POST"])
def search_member(id):
    member_name = None
    member_name = request.form["search"]
    members = []
    members = classes_repository.members(id)
    all_members = members_repository.select_all()
    gym_class = classes_repository.select(id)
    class_name = gym_class.name
    member_ids = classes_repository.member_ids(id)
    number_attendees = len(members)
    return render_template("/classes/booked_members.html", title="Booked members", gym_class=gym_class, class_name=class_name, booked_members=members, all_members=all_members, all_member_ids=member_ids, number_attendees=number_attendees, id=id, member_name=member_name)

@classes_blueprint.route("/classes/member_search", methods=["POST"])
def search_class():
    class_search = None
    class_search = request.form["search"]
    classes = classes_repository.select_all()
    return render_template("/classes/view.html", title="View classes", all_classes=classes, class_search=class_search)
