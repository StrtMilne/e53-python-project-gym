from db.run_sql import run_sql

from models.attendance import Attendance
from models.gym_class import Class
from models.member import Member

def save(attendance):
    sql = "INSERT INTO attendances (member_id, class_id) VALUES (%s, %s) RETURNING *"
    values = [attendance.member_id, attendance.class_id]

    result = run_sql(sql, values)[0]
    id = result["id"]
    attendance.id = id
    return attendance

def update(attendance):
    sql = "UPDATE attendances SET (member_id, class_id) = (%s, %s) WHERE id =%s"
    values = [attendance.member_id, attendance.class_id, attendance.id]
    run_sql(sql, values)
    return attendance

def select_all():
    attendances = []
    sql = "SELECT * FROM attendances"
    results = run_sql(sql)
    for row in results:
        attendance = Attendance(row["member_id"], row["class_id"], row["id"])
        attendances.append(attendance)
    return attendances

def delete_class_in_attendances(id):
    sql = "DELETE FROM attendances WHERE class_id = %s"
    values = [id]
    run_sql(sql, values)