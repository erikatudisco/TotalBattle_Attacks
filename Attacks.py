from captains import Captains
from army import Army
from monsters import Monsters

# %%
class Attack:
    def __init__(self, monster, troops, captain, bonus_strength = 0, bonus_health = 0):
        self.monster = monster
        self.troops = troops
        self.captain = captain
        self.bonus_strength = bonus_strength
        self.bonus_health = bonus_health
        print(f'Monster: {[[m.__class__.__name__, m.amount] for m in self.monster.units ]}')
        print(f'Troops:  {[[m.__class__.__name__, m.amount] for m in self.troops ]}')
        print(f'Captain: {self.captain.__class__.__name__}, level: {self.captain.level}')

    def bonus(self):
        # Check if any type in troops[0].type matches any bonus type in monster[0].bonus
        self.monster_bonus = 0  # Default bonus value
        for bonus in self.monster.units[0].bonus:
            if bonus[0] in self.troops[0].type:  # Checking if bonus type applies to the monster type
                self.monster_bonus += bonus[1]  # Assign bonus value

        # Check if captain's bonus applies to the troop type
        self.captain_bonus_health = 0
        self.captain_bonus_strength = 0
        if self.captain.bonus_health[0] in self.troops[0].type:
            self.captain_bonus_health = self.captain.bonus_health[1]
        if self.captain.bonus_strength[0] in self.troops[0].type:
            self.captain_bonus_strength = self.captain.bonus_strength[1]

        # Check if any type in monster[0].type matches any bonus type in troops[0].bonus
        self.troops_bonus = 0  # Default bonus value
        for bonus in self.troops[0].bonus:
            if bonus[0] in self.monster.units[0].type:  # Checking if bonus type applies to the monster type
                self.troops_bonus = bonus[1]  # Assign bonus value

        self.bonus_troops_health =   1 + self.bonus_health + self.captain_bonus_health
        self.bonus_troops_strength = 1 + self.bonus_strength + self.captain_bonus_strength + self.troops_bonus
        self.bonus_monster = 1 + self.monster_bonus
        print(f'Bonus troops health: {self.bonus_troops_health}')
        print(f'Bonus troops strength: {self.bonus_troops_strength}')
        print(f'Bonus monster: {self.bonus_monster}')

    def attack(self):
        self.bonus()
        self.monster_strength = round(self.monster.units[0].strength * self.monster.units[0].amount*(self.bonus_monster)+0.5)    
        self.monster_health = round(self.monster.units[0].health * self.monster.units[0].amount+0.5)
        print(f'damage from monster {self.monster_strength}')
        print(f'damage needed to kill the monster {self.monster_health}')

        self.troops_health = self.troops[0].health*(self.bonus_troops_health)
        self.troops_strength = self.troops[0].strength*(self.bonus_troops_strength)
        self.troops_loss = round(self.monster_strength/self.troops_health+0.5)
        self.troops_kill = round(self.monster_health/self.troops_strength+0.5)
        self.troops_tot = round( self.troops_loss + self.troops_kill)
        print(f'troops loss: {self.troops_loss}')
        print(f'troops needed to kill the monster: {self.troops_kill}')
        print(f'troops to be sent: {self.troops_tot}')


        

# %%
bonus_strength = 0.905
bonus_health = 0.72

##
monster = Monsters.Inferno(10)
troops = [Army.Archers(3)]
captain = Captains.Bernard(5)

# monster = Monsters.Cursed().common_8
# troops = [Army.Archers(3)]
# captain = Captains.Minamoto(5)

Attack(monster, troops, captain, bonus_strength, bonus_health).attack()
# %%
