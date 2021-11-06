from flask import Flask, render_template, redirect, request, Blueprint
from models.attendance import Attendance

import repositories.classes_repository as classes_repository
import repositories.members_repository as members_repository

attendances_blueprint = Blueprint("attendances", __name__)
