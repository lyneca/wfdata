class ModDrop:
    def __init__(self, name, total_chance):
        self.name = name
        self.total_chance = total_chance
    def __repr__(self):
        return f"ModDrop(\"{self.name}\",{self.total_chance})"
    def __str__(self):
        return f"{self.name:20}: {self.total_chance:.3}%"

class EnemyModDrop(ModDrop):
    def __init__(self, n, e, m, c):
        self.enemy_mod = e
        self.mod_chance = m
        self.mod_chance_name = c
        super().__init__(n, (self.mod_chance/100 * self.enemy_mod/100) * 100)
    def __repr__(self):
        return f"EnemyModDrop(\"{self.name}\",{self.enemy_mod},{self.mod_chance},\"{self.mod_chance_name}\")"
