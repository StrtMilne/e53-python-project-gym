class Member:

    def __init__(self, first_name, last_name, dob, join_date, active=True, premium=False, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.join_date = join_date
        self.active = active
        self.premium = premium
        self.id = id
        self.properties = {
            "first_name": first_name,
            "last_name": last_name,
            "dob": dob,
            "join_date": join_date,
            "active": active,
            "premium": premium,
            "id": id
        }
    
    def __getitem__(self, key):
        return self.properties[key]