from db.run_sql import run_sql

from models.gym_class import Class
from models.member import Member
from datetime import datetime
from helpers.SQL_helpers import most_common


def save(gym_class):
    sql = "INSERT INTO classes (name, type, date, time, capacity, peak) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.type, gym_class.date, gym_class.time, gym_class.capacity, gym_class.peak]
    results = run_sql(sql, values)

    id = results[0]['id']
    gym_class.id = id
    return gym_class

def select_all():
    classes = []
    sql = "SELECT * FROM classes ORDER BY date ASC"
    results = run_sql(sql)

    for row in results:
        gym_class = Class(row["name"], row["type"], row["date"], row["time"], row["capacity"], row["id"])
        classes.append(gym_class)
    return classes
    
def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        time = result["time"]
        gym_class = Class(result["name"], result["type"], result["date"], time, result["capacity"], result["id"])
    return gym_class


def update(gym_class):
    sql = "UPDATE classes SET (name, type, date, time, capacity, peak) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.type, gym_class.date, gym_class.time, gym_class.capacity, gym_class.peak, gym_class.id]
    run_sql(sql, values)
    return gym_class

def members(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN attendances ON attendances.member_id = members.id INNER JOIN classes ON classes.id = attendances.class_id WHERE classes.id = %s ORDER BY date DESC"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["dob"], row["join_date"], row["active"], row["premium"], row["id"])
        members.append(member)
    return members

def member_ids(id):
    member_ids = []
    sql = "SELECT attendances.member_id FROM members INNER JOIN attendances ON attendances.member_id = members.id INNER JOIN classes ON classes.id = attendances.class_id WHERE classes.id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        id = row["member_id"]
        member_ids.append(id)
    return member_ids

def member_remove(member_id, class_id):
    sql = "DELETE FROM attendances WHERE member_id = %s AND class_id = %s"
    values = [member_id, class_id]
    run_sql(sql, values)

def delete_class(id):
    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def total_classes():
    sql = "SELECT * FROM classes"
    total_classes = len(run_sql(sql))
    return total_classes

def most_popular_classes():
    sql = "SELECT classes.name FROM classes INNER JOIN attendances ON classes.id = attendances.class_id INNER JOIN members ON attendances.member_id = members.id"
    list = run_sql(sql)
    name_list = []
    for name in list:
        name_list.append(name[0])
    common_name_list = most_common(name_list)
    class_list = []
    for name in common_name_list:
        class_list.append(name)
    return class_list