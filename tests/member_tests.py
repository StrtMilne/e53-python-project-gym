import unittest
from models.member import Member

class TestMember(unittest.TestCase):

    def test_member_has_first_name(self):
        member_1 = Member("Joe", "Bloggs", "12/5/90", "23/7/21")
        self.assertEqual("Joe", member_1.first_name)

    def test_member_has_last_name(self):
        member_1 = Member("Joe", "Bloggs", "12/5/90", "23/7/21")
        self.assertEqual("Bloggs", member_1.last_name)
    
    def test_member_has_dob(self):
        member_1 = Member("Joe", "Bloggs", "12/5/90", "23/7/21")
        self.assertEqual("12/5/90", member_1.dob)

    def test_member_has_join_date(self):
        member_1 = Member("Joe", "Bloggs", "12/5/90", "23/7/21")
        self.assertEqual("23/7/21", member_1.join_date)
    
    def test_member_has_id(self):
        member_1 = Member("Joe", "Bloggs", "12/5/90", "23/7/21")
        self.assertEqual(None, member_1.id)

    def test_member_has_active_status(self):
        member_1 = Member("Joe", "Bloggs", "12/5/90", "23/7/21")
        self.assertEqual(True, member_1.active)