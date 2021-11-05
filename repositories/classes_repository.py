from db.run_sql import run_sql

from models.gym_class import Class

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
        gym_class = Class(row["name"], row["type"], row["date"], row["time"])
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
