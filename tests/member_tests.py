import unittest
from models.member import Member
from datetime import date

class TestMember(unittest.TestCase):

    def test_member_has_first_name(self):
        member_1 = Member("Joe", "Bloggs", date(1990, 5, 12), date(2021, 7, 23))
        self.assertEqual("Joe", member_1.first_name)

    def test_member_has_last_name(self):
        member_1 = Member("Joe", "Bloggs", date(1990, 5, 12), date(2021, 7, 23))
        self.assertEqual("Bloggs", member_1.last_name)
    
    def test_member_has_dob(self):
        member_1 = Member("Joe", "Bloggs", date(1990, 5, 12), date(2021, 7, 23))
        self.assertEqual(date(1990, 5, 12), member_1.dob)

    def test_member_has_join_date(self):
        member_1 = Member("Joe", "Bloggs", date(1990, 5, 12), date(2021, 7, 23))
        self.assertEqual(date(2021, 7, 23), member_1.join_date)
    
    def test_member_has_id(self):
        member_1 = Member("Joe", "Bloggs", date(1990, 5, 12), date(2021, 7, 23))
        self.assertEqual(None, member_1.id)