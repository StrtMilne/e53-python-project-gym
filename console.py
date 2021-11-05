from models.member import Member
from models.gym_class import Class
import repositories.classes_repository as class_repository
import repositories.members_repository as members_repository

class_1 = Class("Yoga", "Cardio", "11/11/21", "15:30")
class_repository.save(class_1)

class_2 = Class("Weights", "Muscle", "11/11/21", "10:15")
class_repository.save(class_2)

member_1 = Member("Joe", "Bloggs", "12/6/89", "13/8/20")
members_repository.save(member_1)

member_2 = Member("Jane", "Smith", "10/11/80", "15/8/19")
members_repository.save(member_2)