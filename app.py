from flask import Flask, render_template
from db.run_sql import run_sql
from controllers.members_controller import members_blueprint
from controllers.classes_controller import classes_blueprint
import repositories.members_repository as members_repository
import repositories.classes_repository as classes_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)

def most_common(list):
    result = []
    instances = 0
    
    for item in list:
        occurs = list.count(item)
        if occurs == instances:
            result.append(item)
        if occurs > instances:
            result = []
            result.append(item)
    
    return result

@app.route("/")
def index():
#total members
    sql = "SELECT * FROM members"
    total_members = len(run_sql(sql))

#total classes
    sql = "SELECT * FROM classes"
    total_classes = len(run_sql(sql))

#most active members
    sql = "SELECT members.id FROM members INNER JOIN attendances ON members.id = attendances.member_id INNER JOIN classes ON attendances.class_id = classes.id"
    list = run_sql(sql)
    id_list = most_common(list)
    member_list = []
    for id in id_list:
        member = members_repository.select(id[0])
        first_name = member.first_name
        last_name = member.last_name
        name = first_name + " " + last_name
        member_list.append(name)

#most booked class
    sql = "SELECT classes.name FROM classes INNER JOIN attendances ON classes.id = attendances.class_id INNER JOIN members ON attendances.member_id = members.id"
    list = run_sql(sql)
    name_list = most_common(list)
    class_list = []
    for name in name_list:
        class_list.append(name[0])

    return render_template("index.html", title="Home", total_members=total_members, total_classes=total_classes, member_list=member_list, class_list=class_list)

if __name__ == '__main__':
    app.run(debug=True)