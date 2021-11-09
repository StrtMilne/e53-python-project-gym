from flask import Flask, render_template
from db.run_sql import run_sql
from controllers.members_controller import members_blueprint
from controllers.classes_controller import classes_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)

@app.route("/")
def index():
    sql = "SELECT * FROM members"
    total_members = len(run_sql(sql))
    sql = "SELECT * FROM classes"
    total_classes = len(run_sql(sql))
    return render_template("index.html", title="Home", total_members=total_members, total_classes=total_classes)

if __name__ == '__main__':
    app.run(debug=True)