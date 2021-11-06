class Class:

    def __init__(self, name, type, date, time, id=None):
        self.name = name
        self.type = type
        self.date = date
        self.time = time
        self.members = []
        self.id = id

    def add_member_to_class(self, member):
        self.members.append(member)
        return 