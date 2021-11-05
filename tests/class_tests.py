import unittest
from models.gym_class import Class
from datetime import date, time

class TestClass(unittest.TestCase):

    def test_class_has_name(self):
        class_1 = Class("Yoga", "Cardio", "16/11/21", "15:30")
        self.assertEqual("Yoga", class_1.name)

    def test_class_has_type(self):
        class_1 = Class("Yoga", "Cardio", "16/11/21", "15:30")
        self.assertEqual("Cardio", class_1.type)

    def test_class_has_date(self):
        class_1 = Class("Yoga", "Cardio", "16/11/21", "15:30")
        self.assertEqual("16/11/21", class_1.date)

    def test_class_has_time(self):
        class_1 = Class("Yoga", "Cardio", "16/11/21", "15:30")
        self.assertEqual("15:30", class_1.time)

    
