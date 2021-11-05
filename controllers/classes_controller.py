from flask import Flask, render_template, redirect, request, Blueprint
from models.gym_class import Class

import repositories.classes_repository as classes_repository

classes_blueprint = Blueprint("classes", __name__)

@classes_blueprint.route("/classes")
def classes():
    classes = classes_repository.select_all()
    return render_template("/classes/view.html", all_classes=classes)

@classes_blueprint.route("/classes/<id>/edit")
def edit_class(id):
    gym_class = classes_repository.select(id)
    return render_template("/classes/edit.html", gym_class=gym_class)