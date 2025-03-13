class Captains:

    class Bernard:
        def __init__(self, level) -> None:
            self.level = level
            self.bonus_strength = ['Ranged', self.level/100]
            self.bonus_health = ['Ranged', self.level/100]

    def __init__(self):
        pass


class Army:

    class Archers:
        level_data = {
            1: [30, 100, [["Meele", 1.17], ["Flying", 1.51]]],
            2: [100, 300, [["Meele", 1.13]]],  # Example for level 2
            3: [160, 480, [["Meele", 1.17], ["Flying", 1.51]]],
        }

        def __init__(self, level, amount=1):
            self.type = ["Guardsman", "Human", "Ranged"]
            if level in self.level_data:
                self.strength, self.health, self.bonus = self.level_data[level]
            else:
                raise ValueError(f"Invalid level {level} for Archers.")
            self.amount = amount


class Fiend:
    def __init__(self, amount = 1):
        self.type = ["Demon",	"Meele"]
        self.strength = 28
        self.health = 84
        self.bonus = [["Mounted",	0.15]]
        self.amount = amount


class Inferno:

    def __init__(self):
        self.common_5 = [Fiend(500)]

bonus_strength = 0.905
bonus_health = 0.72

##
monster = Inferno().common_5
monster_strength = monster[0].strength * monster[0].amount
monster_health = monster[0].health * monster[0].amount
print(f'damage from monster {monster_strength}')
print(f'damage needed to kill the monster {monster_health}')
troops = [Army().Archers(3)]
captain = Captains.Bernard(8)
# Default bonus value
captain_bonus_health = 0

# Check if captain's bonus applies to the troop type
if captain.bonus_health[0] in troops[0].type:
    captain_bonus_health = captain.bonus_health[1]
if captain.bonus_strength[0] in troops[0].type:
    captain_bonus_strength = captain.bonus_health[1]

# Check if any type in monster[0].type matches any bonus type in troops[0].bonus
troops_bonus = 0  # Default bonus value

for bonus in troops[0].bonus:
    if bonus[0] in monster[0].type:  # Checking if bonus type applies to the monster type
        troops_bonus = bonus[1]  # Assign bonus value
print(1+bonus_health+captain_bonus_health)
print(1+bonus_strength+captain_bonus_strength+troops_bonus)

troops_health = troops[0].health*(1+bonus_health+captain_bonus_health)
troops_strength = troops[0].strength*(1+bonus_strength+captain_bonus_strength+troops_bonus)
troops_loss = monster_strength/troops_health
troops_kill = monster_health/troops_strength
troops_tot = troops_loss + troops_kill
print(f'troops loss: {troops_loss}')
print(f'troops needed to kill the monster: {troops_kill}')
print(f'troops to be sent: {troops_tot}')