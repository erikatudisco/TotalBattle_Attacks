class Army:

    class Archers:
        level_data = {
            1: [ 50, 150, [["Melee", 0.52], ["Flying", 0.67]]],
            2: [ 90, 270, [["Melee", 0.78], ["Flying", 1.01]]],
            3: [160, 480, [["Melee", 1.17], ["Flying", 1.51]]],
        }

        def __init__(self, level, amount=0):
            self.type = ["Guardsman", "Human", "Ranged"]
            if level in self.level_data:
                self.strength, self.health, self.bonus = self.level_data[level]
            else:
                raise ValueError(f"Invalid level {level} for Archers.")
            self.amount = amount

    class Spearman:
        level_data = {
            1: [ 50, 150, [["Mounted", 0.39], ["Beast", 0.8]]],
            2: [ 90, 270, [["Mounted", 0.59], ["Beast", 1.2]]],
            3: [160, 480, [["Mounted", 0.88], ["Beast", 1.8]]],
        }

        def __init__(self, level, amount=0):
            self.type = ["Guardsman", "Human", "Melee"]
            if level in self.level_data:
                self.strength, self.health, self.bonus = self.level_data[level]
            else:
                raise ValueError(f"Invalid level {level} for Spearman.")
            self.amount = amount

    class Rider:
        level_data = {
            1: [100,  300, [["Ranged", 0.65], ["Siege", 0.54]]],
            2: [180,  540, [["Ranged", 0.98], ["Siege", 0.81]]],
            3: [320,  960, [["Ranged", 1.46], ["Siege", 1.22]]],
        }

        def __init__(self, level, amount=0):
            self.type = ["Guardsman", "Human", "Mounted"]
            if level in self.level_data:
                self.strength, self.health, self.bonus = self.level_data[level]
            else:
                raise ValueError(f"Invalid level {level} for Rider.")
            self.amount = amount
