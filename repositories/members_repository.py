from db.run_sql import run_sql

from models.member import Member

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
    sql = "SELECT * FROM members where id = %s"
    values = [id]
    results = run_sql(sql, values)

    id = results[0]["id"]
    member.id = id
    return member