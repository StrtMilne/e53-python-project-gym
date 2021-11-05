from flask import Flask, render_template, redirect, Blueprint
from models.member import Member
from models.gym_class import Class

import repositories.members_repository as member_repository
import repositories.classes_repository as classes_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("/members/view.html", all_members=members)

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    render_template("/edit.html", member=member)

@members_blueprint.route("/members/<id>/edit", methods=["POST"]
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    