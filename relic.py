class Relic:
    def __init__(self, era, name, drops):
        self.era = era
        self.name = name
        self.drops = drops

    def __repr__(self):
        return f"Relic(\"{self.era}\",\"{self.name}\",{repr(self.drops)})"

    def __str__(self):
        return f"{self.era} {self.name}"

class RelicDrop:
    def __init__(self, relic, part, chance):
        self.relic = relic
        self.part = part
        self.chance = chance
