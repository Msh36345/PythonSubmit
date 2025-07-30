
class Agent:
    def __init__(self, code_name, real_name, location, id=None, status="Active", mission_completed=0):
        self.id=id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.id = id
        self.status = status
        self.mission_completed = mission_completed

    def __str__(self):
        return f"""\033[35mId = {self.id}
Code name = {self.code_name}
    Real name = {self.real_name}
    Location = {self.location}
    Status = {self.status}
    Mission completed = {self.mission_completed}\033[0m"""


