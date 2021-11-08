from db.run_sql import run_sql

from models.gym_class import Class
from models.member import Member


def save(gym_class):
    sql = "INSERT INTO classes (name, type, date, time) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [gym_class.name, gym_class.type, gym_class.date, gym_class.time]
    results = run_sql(sql, values)

    id = results[0]['id']
    gym_class.id = id
    return gym_class

def select_all():
    classes = []
    sql = "SELECT * FROM classes"
    results = run_sql(sql)

    for row in results:
        gym_class = Class(row["name"], row["type"], row["date"], row["time"], row["id"])
        classes.append(gym_class)
    return classes
    
def select(id):
    gym_class = None
    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Class(result["name"], result["type"], result["date"], result["time"], result["id"])
    return gym_class


def update(gym_class):
    sql = "UPDATE classes SET (name, type, date, time) = (%s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.type, gym_class.date, gym_class.time, gym_class.id]
    run_sql(sql, values)
    return gym_class

def members(id):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN attendances ON attendances.member_id = members.id INNER JOIN classes ON classes.id = attendances.class_id WHERE classes.id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["dob"], row["join_date"], row["id"])
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