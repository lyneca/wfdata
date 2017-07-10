class ModDrop:
    """
    Superclass for mod drops
    """
    def __init__(self, dropped_by, name, total_chance):
        self.dropped_by = dropped_by
        self.name = name
        self.total_chance = total_chance

    def __repr__(self):
        return f"ModDrop(\"{self.dropped_by}\",\"{self.name}\",{self.total_chance})"

    def __str__(self):
        return f"{self.dropped_by:.<40}: {self.total_chance:.3}%"


class EnemyModDrop(ModDrop):
    """
    Class for mods and blueprints that drop from enemies
    """
    def __init__(self, e, n, em, m, c):
        """
        :param e: Name of enemy that drops the mod
        :param en: Name of mod
        :param em: Percentage chance of the enemy dropping a mod
        :param m: Percentage chance that if the enemy drops a mod, it will be this one
        :param c: "Chance name" - Common, Uncommon, Rare, Legendary, etc
        """
        self.enemy_mod = em
        self.mod_chance = m
        self.mod_chance_name = c
        super().__init__(e, n, (self.mod_chance/100 * self.enemy_mod/100) * 100)

    def __repr__(self):
        return f"EnemyModDrop(\"{self.dropped_by}\",\"{self.name}\",{self.enemy_mod},{self.mod_chance},\"{self.mod_chance_name}\")"


class MissionDrop(ModDrop):
    """
    Class for mods and items that drop from missions
    """
    def __init__(self, m, n, r, c):
        """
        :param m: Mission name
        :param n: Item/Mod name
        :param r: Rotation (or '' if not applicable)
        :param c: Drop chance of the mod
        """
        super().__init__(m, n, c)
        self.rotation = r

    def __repr__(self):
        return f"MissionDrop(\"{self.dropped_by}\",\"{self.name}\",\"{self.rotation}\",{self.total_chance})"

    def __str__(self):
        return f"{self.dropped_by + ('/' + self.rotation if self.rotation else ''):.<40}: {self.total_chance:.3}%"

    def reverseName(self):
        return f"{((self.rotation if self.rotation else '') + ': ' + self.name):.<40}: {self.total_chance:.3}%"
