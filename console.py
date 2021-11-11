from controllers import members_controller
from models.attendance import Attendance
from models.member import Member
from models.gym_class import Class
from repositories import attendances_repository
import repositories.classes_repository as classes_repository
import repositories.members_repository as members_repository
import controllers.classes_controller as classes_controller
from datetime import date, time

import pdb

class_1 = Class("Yoga", "Cardio", date(2021, 11, 14), time(15, 30), 12)
classes_repository.save(class_1)

class_2 = Class("Weights", "Muscle", date(2021, 11, 17), time(10, 30), 6)
classes_repository.save(class_2)

class_3 = Class("Yoga", "Cardio", date(2021, 12, 14), time(8, 30), 12)
classes_repository.save(class_3)

class_4 = Class("Weights", "Muscle", date(2021, 11, 24), time(18, 30), 6)
classes_repository.save(class_4)

class_5 = Class("Swimming", "Cardio", date(2021, 12, 23), time(7, 30), 20)
classes_repository.save(class_5)

class_6 = Class("Pilates", "Cardio", date(2021, 11, 29), time(11, 45), 15)
classes_repository.save(class_6)

class_7 = Class("Circuits", "Mixed", date(2021, 11, 23), time(13, 5), 10)
classes_repository.save(class_5)

class_8 = Class("Machines", "Muscle", date(2021, 11, 21), time(16, 15), 6)
classes_repository.save(class_6)


member_1 = Member("Joe", "Bloggs", "12/6/89", "13/8/20")
members_repository.save(member_1)

member_2 = Member("Jane", "Smith", "10/11/80", "15/8/19")
members_repository.save(member_2)

member_3 = Member("Ian", "Anderson", "12/1/92", "19/3/19")
members_repository.save(member_3)

member_4 = Member("Roger", "Boyd", "10/11/94", "20/4/17")
members_repository.save(member_4)

member_5 = Member("Sarah", "McGregor", "12/8/79", "13/8/21")
members_repository.save(member_5)

member_6 = Member("James", "Mill", "09/11/80", "19/8/19")
members_repository.save(member_6)

member_7 = Member("Joanne", "Boyd", "10/11/94", "20/4/17")
members_repository.save(member_7)

member_8 = Member("Victor", "McGregor", "12/8/79", "13/8/21")
members_repository.save(member_8)

member_9 = Member("Alan", "Mill", "09/11/80", "19/8/19")
members_repository.save(member_9)

attendance_1 = Attendance(1, 2)
attendances_repository.save(attendance_1)

attendance_2 = Attendance(1, 4)
attendances_repository.save(attendance_1)

attendance_3 = Attendance(1, 2)
attendances_repository.save(attendance_1)

attendance_4 = Attendance(2, 3)
attendances_repository.save(attendance_1)

attendance_5 = Attendance(2, 2)
attendances_repository.save(attendance_1)

attendance_6 = Attendance(3, 2)
attendances_repository.save(attendance_1)

pdb.set_trace()