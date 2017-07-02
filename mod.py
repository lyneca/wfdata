class EnemyModDrop:
    def __init__(self, n, e, m, c):
        self.name = n
        self.enemy_mod = e
        self.mod_chance = m
        self.mod_chance_name = c
        self.total_chance = (self.mod_chance/100 * self.enemy_mod/100) * 100
    def __repr__(self):
        return f"EnemyModDrop(\"{self.name}\",{self.enemy_mod},{self.mod_chance},\"{self.mod_chance_name}\")"
