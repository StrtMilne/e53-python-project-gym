from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Class
import repositories.classes_repository as classes_repository

from helpers.SQL_helpers import most_common

def save(member):
    sql = "INSERT INTO members (first_name, last_name, dob, join_date, active, premium) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.dob, member.join_date, member.active, member.premium]
    results = run_sql(sql, values)

    id = results[0]["id"]
    member.id = id
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members ORDER BY active DESC, last_name ASC, first_name"
    results = run_sql(sql)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["dob"], row["join_date"], row["active"], row["premium"], row["id"])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result["first_name"], result["last_name"], result["dob"], result["join_date"], result["active"], result["premium"], result["id"])
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, dob, join_date, active, premium) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.dob, member.join_date, member.active, member.premium, member.id]
    run_sql(sql, values)
    return member

def classes(id):
    classes = []
    sql = "SELECT classes.* FROM classes INNER JOIN attendances ON attendances.class_id = classes.id INNER JOIN members ON members.id = attendances.member_id WHERE members.id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Class(row["name"], row["type"], row["date"], row["time"], row["capacity"], row["id"])
        gym_class.members = classes_repository.member_ids(row["id"])
        classes.append(gym_class)
    return classes

def unbooked_classes(id):
    classes = []
    sql = "SELECT DISTINCT classes.* FROM classes INNER JOIN attendances ON attendances.member_id = classes.id INNER JOIN members ON members.id = attendances.member_id WHERE NOT members.id = %s"
    values = [id]

    results = run_sql(sql, values)

    for row in results:
        gym_class = Class(row["name"], row["type"], row["date"], row["time"], row["capacity"], row["peak"], row["id"])
        gym_class.members = classes_repository.member_ids(row["id"])
        classes.append(gym_class)
    return classes

def class_remove(member_id, class_id):
    sql = "DELETE FROM attendances WHERE member_id = %s AND class_id = %s"
    values = [member_id, class_id]
    run_sql(sql, values)

def class_ids(id):
    class_ids = []
    sql = "SELECT attendances.class_id FROM classes INNER JOIN attendances ON attendances.class_id = classes.id INNER JOIN members ON members.id = attendances.member_id WHERE members.id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        id = row["class_id"]
        class_ids.append(id)
    return class_ids

def total_members():
    sql = "SELECT * FROM members"
    total_members = len(run_sql(sql))
    return total_members

def most_active_members():
    sql = "SELECT members.id FROM members INNER JOIN attendances ON members.id = attendances.member_id INNER JOIN classes ON attendances.class_id = classes.id"
    list = run_sql(sql)
    id_list = []
    for id in list:
        id_list.append(id[0])
    common_id_list = most_common(id_list)
    member_list = []
    for id in common_id_list:
        member = select(id)
        first_name = member.first_name
        last_name = member.last_name
        name = first_name + " " + last_name
        member_list.append(name)
    return member_list