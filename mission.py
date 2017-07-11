class GenericDropLocation:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"GenericDropLocation(\"{self.name}\")"

    def __str__(self):
        return f"{self.name}"

class Mission:
    def __init__(self, planet, name, mission_type, event=False):
        self.planet = planet
        self.name = name
        self.mission_type = mission_type
        self.event = event
    
    def __repr__(self):
        return f"Mission(\"{self.planet}\",\"{self.name}\",\"{self.mission_type}\",{self.event})"

#   def __str__(self):
#       return ("[EVENT] " if self.event else '') + \
#           f"[{self.mission_type}] {self.planet}/{self.name}"

    def __str__(self):
        return f"{'[Event ' if self.event else '['}{self.mission_type:}] {self.planet}/{self.name}"
