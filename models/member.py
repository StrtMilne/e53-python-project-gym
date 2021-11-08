class Member:

    def __init__(self, first_name, last_name, dob, join_date, active=True, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.join_date = join_date
        self.active = active
        self.id = id