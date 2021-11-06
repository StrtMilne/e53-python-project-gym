from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Class

def save(member):
    sql = "INSERT INTO members (first_name, last_name, dob, join_date) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.first_name, member.last_name, member.dob, member.join_date]
    results = run_sql(sql, values)

    id = results[0]["id"]
    member.id = id
    return member

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["dob"], row["join_date"], row["id"])
        members.append(member)

    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result["first_name"], result["last_name"], result["dob"], result["join_date"], result["id"])
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, dob, join_date) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.dob, member.join_date, member.id]
    run_sql(sql, values)
    return member

def classes(id):
    classes = []
    sql = "SELECT classes.* FROM classes INNER JOIN attendances ON attendances.member_id = classes.id INNER JOIN members ON members.id = attendances.member_id WHERE members.id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Class(row["name"], row["type"], row["date"], row["time"], row["id"])
        classes.append(gym_class)
    return classes

def unbooked_classes(id):
    classes = []
    sql = "SELECT DISTINCT classes.* FROM classes INNER JOIN attendances ON attendances.member_id = classes.id INNER JOIN members ON members.id = attendances.member_id WHERE NOT members.id = %s"
    values = [id]

    results = run_sql(sql, values)

    for row in results:
        gym_class = Class(row["name"], row["type"], row["date"], row["time"], row["id"])
        classes.append(gym_class)
    return classes