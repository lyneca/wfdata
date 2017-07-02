class ModDrop:
    def __init__(self, dropped_by, name, total_chance):
        self.dropped_by = dropped_by
        self.name = name
        self.total_chance = total_chance
    def __repr__(self):
        return f"ModDrop(\"{self.dropped_by}\",\"{self.name}\",{self.total_chance})"
    def __str__(self):
        return f"{self.dropped_by:30}: {self.total_chance:.3}%"

class EnemyModDrop(ModDrop):
    def __init__(self, e, n, em, m, c):
        self.enemy_mod = em
        self.mod_chance = m
        self.mod_chance_name = c
        super().__init__(e, n, (self.mod_chance/100 * self.enemy_mod/100) * 100)
    def __repr__(self):
        return f"EnemyModDrop(\"{self.dropped_by}\",\"{self.name}\",{self.enemy_mod},{self.mod_chance},\"{self.mod_chance_name}\")"

class MissionDrop(ModDrop):
    def __init__(self, m, n, r, c):
        super().__init__(m, n, c)
        self.rotation = r
    def __repr__(self):
        return f"MissionDrop(\"{self.dropped_by}\",\"{self.name}\",\"{self.rotation}\",{self.total_chance})"
    def __str__(self):
        return f"{self.dropped_by + ('/' + self.rotation if self.rotation else ''):30}: {self.total_chance:.3}%"
