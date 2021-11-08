class Class:

    def __init__(self, name, type, date, time, capacity, id=None):
        self.name = name
        self.type = type
        self.date = date
        self.time = time
        self.capacity = capacity
        self.members = []
        self.id = id

    def add_member_to_class(self, id):
        self.members.append(id)