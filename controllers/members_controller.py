from flask import Flask, render_template, redirect, Blueprint, request
from models.member import Member
from models.gym_class import Class
from models.attendance import Attendance

import repositories.members_repository as members_repository
import repositories.classes_repository as classes_repository
import repositories.attendances_repository as attendances_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = members_repository.select_all()
    return render_template("/members/view.html", title="All members", all_members=members)

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = members_repository.select(id)
    return render_template("members/edit.html", title="Edit member", member=member)

@members_blueprint.route("/members/<id>/edit", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    dob = request.form["dob"]
    join_date = request.form["join_date"]
    if request.form["member-status"] == "active":
        active = True
    else:
        active = False

    if request.form["premium-status"] == "premium":
        premium = True
    else:
        premium = False

    member = Member(first_name, last_name, dob, join_date, active, premium, id)
    members_repository.update(member)

    classes = []
    classes = members_repository.classes(id)
    all_classes = classes_repository.select_all()
    class_ids = members_repository.class_ids(id)

    return render_template("/members/booked_classes.html", title="Booked classes", member=member, booked_classes=classes, all_classes=all_classes, all_class_ids=class_ids, member_id=id)

@members_blueprint.route("/members/new")
def add_member():
    return render_template("/members/new.html", title="Add new member")

@members_blueprint.route("/members/new", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    dob = request.form["dob"]
    join_date = request.form["join_date"]
    active = True
    if request.form["premium-status"] == "premium":
        premium = True
    if request.form["premium-status"] == "standard":
        premium = False
    member = Member(first_name, last_name, dob, join_date, active, premium)
    members_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/view")
def booked_classes(id):
    classes = []
    classes = members_repository.classes(id)
    all_classes = classes_repository.select_all()
    class_ids = members_repository.class_ids(id)
    member = members_repository.select(id)
    return render_template("/members/booked_classes.html", title="Booked classes", member=member, booked_classes=classes, all_classes=all_classes, all_class_ids=class_ids, member_id=id)

@members_blueprint.route("/members/booked_classes/<member_id>/<class_id>/remove")
def remove_member(member_id, class_id):
    classes_repository.member_remove(member_id, class_id)

    classes = []
    classes = members_repository.classes(member_id)
    all_classes = classes_repository.select_all()
    class_ids = members_repository.class_ids(member_id)
    member = members_repository.select(member_id)
    return render_template("/members/booked_classes.html", title="Booked classes", member=member, booked_classes=classes, all_classes=all_classes, all_class_ids=class_ids, member_id=member_id)

@members_blueprint.route("/members/<member_id>/booked_classes", methods=["POST"])
def add_multiple_classes(member_id):
    classes = []
    classes = request.form.to_dict(flat=False)["class_id"]
    
    for row in classes:
        attendance = Attendance(member_id, row)
        attendances_repository.save(attendance)
    
    classes = []
    classes = members_repository.classes(member_id)
    all_classes = classes_repository.select_all()
    class_ids = members_repository.class_ids(member_id)
    member = members_repository.select(member_id)
    return render_template("/members/booked_classes.html", title="Booked classes", member=member, booked_classes=classes, all_classes=all_classes, all_class_ids=class_ids, member_id=member_id)