class Captains:

    class Bernard:
        def __init__(self, level) -> None:
            self.level = level
            self.bonus_health = ['Ranged', self.level/100]
            self.bonus_strength = ['Ranged', self.level/100]

    class Minamoto:
        def __init__(self, level) -> None:
            self.level = level
            self.bonus_health = ['Ranged', self.level/100]
            self.bonus_strength = ['Ranged', 2 * self.level/100]

    def __init__(self):
        self.leadership = ([100, 125, 150, 200, 250, 500, 750, 1000, 1250, 1500] +   # Levels 1-10
                           [1750, 2000, 2150, 2250, 2350, 2450, 2550, 2600, 2650, 2725] +  # Levels 11-20
                           [2800, 2875, 2950, 3025, 3100, 3175, 3300, 3375, 3475, 3575] +  # Levels 21-30
                           [3675, 3775, 3875, 3975, 4075, 4175, 4275, 4400, 4525, 4650] +  # Levels 31-40
                           list(range(4800, 10000, 250)) +  # Levels 41-100
                           list(range(10250, 20000, 500)) +  # Levels 101-200
                           list(range(20500, 30000, 1000)) +  # Levels 201-300
                           list(range(31000, 50000, 2000))  # Levels 301-500                          
                           )
        self.dominance = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        self.authority = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]


class Army:

    class Archers:
        level_data = {
            1: [ 50, 150, [["Melee", 0.52], ["Flying", 0.67]]],
            2: [ 90, 270, [["Melee", 0.78], ["Flying", 1.01]]],
            3: [160, 480, [["Melee", 1.17], ["Flying", 1.51]]],
        }

        def __init__(self, level, amount=1):
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

        def __init__(self, level, amount=1):
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

        def __init__(self, level, amount=1):
            self.type = ["Guardsman", "Human", "Mounted"]
            if level in self.level_data:
                self.strength, self.health, self.bonus = self.level_data[level]
            else:
                raise ValueError(f"Invalid level {level} for Rider.")
            self.amount = amount

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


class Inferno:

    def __init__(self):
        self.common_5 = [Monster_units.Fiend(500)]

class Cursed:
    
    def __init__(self):
        self.common_8 = [Monster_units.Withch_Doctor(330)]

class Undead:
    
    def __init__(self):
        self.common_6 = [Monster_units.Banshee(210)]

bonus_strength = 0.905
bonus_health = 0.72

##
monster = Inferno().common_5
troops = [Army.Archers(3)]
captain = Captains.Bernard(5)
print(f'Monster: {monster}')
print(f'Troops: {troops}')
print(f'Captain: {captain}')

monster = Cursed().common_8
troops = [Army.Archers(3)]
captain = Captains.Minamoto(5)
print(f'Monster: {[m.__class__.__name__ for m in monster]}')
print(f'Troops: {troops.__class__.__name__}')
print(f'Captain: {captain.__class__.__name__}')


# Check if any type in troops[0].type matches any bonus type in monster[0].bonus
monster_bonus = 0  # Default bonus value
for bonus in monster[0].bonus:
    if bonus[0] in troops[0].type:  # Checking if bonus type applies to the monster type
        monster_bonus += bonus[1]  # Assign bonus value

# Check if captain's bonus applies to the troop type
captain_bonus_health = 0
captain_bonus_strength = 0
if captain.bonus_health[0] in troops[0].type:
    captain_bonus_health = captain.bonus_health[1]
if captain.bonus_strength[0] in troops[0].type:
    captain_bonus_strength = captain.bonus_health[1]

# Check if any type in monster[0].type matches any bonus type in troops[0].bonus
troops_bonus = 0  # Default bonus value

for bonus in troops[0].bonus:
    if bonus[0] in monster[0].type:  # Checking if bonus type applies to the monster type
        troops_bonus = bonus[1]  # Assign bonus value

bonus_troops_health = 1+bonus_health+captain_bonus_health
bonus_troops_strength = 1+bonus_strength+captain_bonus_strength+troops_bonus
bonus_monster = 1+monster_bonus
print(f'Bonus troops health: {bonus_troops_health}')
print(f'Bonus troops strength: {bonus_troops_strength}')
print(f'Bonus monster: {bonus_monster}')

monster_strength = round(monster[0].strength * monster[0].amount*(bonus_monster)+0.5)
monster_health = round(monster[0].health * monster[0].amount+0.5)
print(f'damage from monster {monster_strength}')
print(f'damage needed to kill the monster {monster_health}')

troops_health = troops[0].health*(bonus_troops_health)
troops_strength = troops[0].strength*(bonus_troops_strength)
troops_loss = round(monster_strength/troops_health+0.5)
troops_kill = round(monster_health/troops_strength+0.5)
troops_tot = round( troops_loss + troops_kill)
print(f'troops loss: {troops_loss}')
print(f'troops needed to kill the monster: {troops_kill}')
print(f'troops to be sent: {troops_tot}')