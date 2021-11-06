from flask import Flask, render_template, redirect, Blueprint, request
from models.member import Member
from models.gym_class import Class

import repositories.members_repository as members_repository
import repositories.classes_repository as classes_repository

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
    member = Member(first_name, last_name, dob, join_date, id)
    members_repository.update(member)
    return redirect("/members")

@members_blueprint.route("/members/new")
def add_member():
    return render_template("/members/new.html", title="Add new member")

@members_blueprint.route("/members/new", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    dob = request.form["dob"]
    join_date = request.form["join_date"]
    member = Member(first_name, last_name, dob, join_date)
    members_repository.save(member)

    return redirect("/members")

@members_blueprint.route("/members/<id>/view")
def booked_classes(id):
    classes = []
    classes = members_repository.classes(id)
    # unbooked_classes = members_repository.unbooked_classes(id) #Probably not needed
    all_classes = classes_repository.select_all()
    member = members_repository.select(id)
    return render_template("/members/booked_classes.html", title="Booked classes", member=member, booked_classes=classes, all_classes=all_classes)
