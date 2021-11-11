from flask import Flask, render_template
from controllers.members_controller import members_blueprint
from controllers.classes_controller import classes_blueprint
import repositories.members_repository as members_repository
import repositories.classes_repository as classes_repository
from helpers.SQL_helpers import most_common

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)

@app.route("/")
def index():

    total_members = members_repository.total_members()

    total_classes = classes_repository.total_classes()

    member_list = members_repository.most_active_members()

    class_list = classes_repository.most_popular_classes()

    return render_template("index.html", title="Home", total_members=total_members, total_classes=total_classes, member_list=member_list, class_list=class_list)

if __name__ == '__main__':
    app.run(debug=True)