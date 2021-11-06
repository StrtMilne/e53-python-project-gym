from flask import Flask, render_template
from controllers.members_controller import members_blueprint
from controllers.classes_controller import classes_blueprint
from controllers.attendances_controller import attendances_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)
app.register_blueprint(attendances_blueprint)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)