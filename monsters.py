class Monster_units:

    class Fiend:
        def __init__(self, amount = 1):
            self.type = ["Demon", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.15]]
            self.amount = amount
    
    class Withch_Doctor:
        def __init__(self, amount = 1):
            self.type = ["Cursed", "Ranged"]
            self.strength = 150
            self.health = 450
            self.bonus = [["Melee", 0.25]]
            self.amount = amount
    
    class Banshee:
        def __init__(self, amount = 1):
            self.type = ["Undead", "Ranged"]
            self.strength = 100
            self.health = 300
            self.bonus = [["Melee", 0.45]]
            self.amount = amount

class Monsters:
    class Inferno:
        level_data = {
            5:  [Monster_units.Fiend(500)],
            10: [Monster_units.Fiend(1000), Monster_units.Withch_Doctor(100)],
        }

        def __init__(self, level):
            if level in self.level_data:
                self.units = self.level_data[level]
            else:
                raise ValueError(f"Invalid level {level} for Inferno.")

    class Cursed:
        
        def __init__(self):
            self.common_8 = [Monster_units.Withch_Doctor(330)]

    class Undead:
        
        def __init__(self):
            self.common_6 = [Monster_units.Banshee(210)]
