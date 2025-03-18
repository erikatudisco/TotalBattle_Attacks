import copy

class Monster_units:
    
    class Banshee:
        def __init__(self, amount = 1):
            self.type = ["Undead", "Ranged"]
            self.strength = 100
            self.health = 300
            self.bonus = [["Melee", 0.45]]
            self.amount = amount

    class Dwarf:
        def __init__(self, amount = 1):
            self.type = ["Elves", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.15]]
            self.amount = amount
    
    class Elven_Archer:
        def __init__(self, amount = 1):
            self.type = ["Elves", "Ranged"]
            self.strength = 100
            self.health = 300
            self.bonus = [["Melee", 0.35]]
            self.amount = amount

    class Fiend:
        def __init__(self, amount = 1):
            self.type = ["Demon", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.15]]
            self.amount = amount

    class Ghoul:
        def __init__(self, amount = 1):
            self.type = ["Beast","Undead", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.10]]
            self.amount = amount

    class Goblin:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Melee"]
            self.strength = 28
            self.health = 84
            self.bonus = [["Mounted", 0.10]]
            self.amount = amount

    class Magog:
        def __init__(self, amount = 1):
            self.type = ["Demon", "Ranged"]
            self.strength = 50
            self.health = 150
            self.bonus = [["Melee", 0.30]]
            self.amount = amount
    
    class Withch_Doctor:
        def __init__(self, amount = 1):
            self.type = ["Cursed", "Ranged"]
            self.strength = 150
            self.health = 450
            self.bonus = [["Melee", 0.25]]
            self.amount = amount

    class Wolf_Rider:
        def __init__(self, amount = 1):
            self.type = ["Barbarian", "Mounted"]
            self.strength = 150
            self.health = 450
            self.bonus = [["Ranged", 0.6],[ "Siege", 0.4]]
            self.amount = amount

class Monsters:

    class Barbarian:
        level_data = {
            12:  [Monster_units.Wolf_Rider(1200), Monster_units.Goblin(2800)],
        }

        def __init__(self, level):
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Barbarian.")

    class Cursed:
        level_data = {
            8:  [Monster_units.Withch_Doctor(330)],
        }
        
        def __init__(self):
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Cursed.")
            
    class Elf:
        level_data = {
            2:  [Monster_units.Dwarf(700)],
            7:  [Monster_units.Elven_Archer(300)],
            11: [Monster_units.Elven_Archer(1200), Monster_units.Dwarf(1900)],
        }
        
        def __init__(self, level):
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Elf.")
    
    class Inferno:
        level_data = {
            5:  [Monster_units.Fiend(500)],
            10: [Monster_units.Magog(2300)],
        }

        def __init__(self, level):
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Inferno.")

    class Undead:
        level_data = {
            1:  [Monster_units.Ghoul(93)],
            6:  [Monster_units.Banshee(210)],
        }
        
        def __init__(self):
            if level in self.level_data:
                self.units = copy.deepcopy(self.level_data[level])
            else:
                raise ValueError(f"Invalid level {level} for Undead.")
