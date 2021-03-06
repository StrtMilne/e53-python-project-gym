from datetime import time, datetime

class Class:

    def __init__(self, name, type, date, time, capacity, id=None):
        self.name = name
        self.type = type
        self.date = date
        self.time = time
        self.capacity = capacity
        self.members = []
        self.peak = self.peak_time(self.time)
        self.id = id

    def add_member_to_class(self, id):
        self.members.append(id)

    def peak_time(self, booking):
        if time(9, 00) <= booking <= time(17, 00):
            return False
        else:
            return True