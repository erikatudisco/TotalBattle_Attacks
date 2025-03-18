# %%
import importlib
import army as a
import monsters as m
import captains as c
importlib.reload(a)
importlib.reload(m)
importlib.reload(c)

# %%
class Attack:
    def __init__(self, monster, troops, captain, bonus_strength = 0, bonus_health = 0):
        self.monster = monster
        self.troops = troops
        self.captain = captain
        self.bonus_strength = bonus_strength
        self.bonus_health = bonus_health
        self.troops_needed = [0]*len(troops)
        print(f'Monster: {[[i.__class__.__name__, i.amount]          for i in self.monster.units ]}')
        print(f'Troops:  {[[i.__class__.__name__, i.level, i.amount] for i in self.troops ]}')
        print(f'Captain: {self.captain.__class__.__name__}, level: {self.captain.level}')

    def round_order(self):
        self.monster_strength = [0]*len(self.monster.units)
        # Calculate the strength of the monster units
        for m_index in range(len(self.monster.units)):
            self.monster_strength[m_index] =  round(self.monster.units[m_index].strength * self.monster.units[m_index].amount+0.5)    
            
        self.monster_order = sorted(range(len(self.monster_strength)), key=lambda i: self.monster_strength[i], reverse=True)

        # Calculate the strength of the troops units
        self.troops_strength = [0]*len(self.troops)
        for t_index in range(len(self.troops)):
            self.troops_strength[t_index] = round(self.troops[t_index].strength*self.troops[t_index].amount+0.5)   

        self.troops_order = sorted(range(len(self.troops_strength)), key=lambda i: self.troops_strength[i], reverse=True)

        print(f'Monster order: {[self.monster.units[i].__class__.__name__ for i in self.monster_order]}')
        print(f'Troops order: {[[self.troops[i].__class__.__name__, self.troops[i].level] for i in self.troops_order]}')
    
    def bonus(self, monster_unit, troops_unit, captain):

        # Check if any type in troops[0].type matches any bonus type in monster[0].bonus
        self.monster_bonus = 0  # Default bonus value
        for bonus in monster_unit.bonus:
            if bonus[0] in troops_unit.type:  # Checking if bonus type applies to the monster type
                self.monster_bonus += bonus[1]  # Assign bonus value

        # Check if captain's bonus applies to the troop type
        captain_bonus_strength = 0
        captain_bonus_health = 0
        if captain.bonus_strength[0] in troops_unit.type:
            captain_bonus_strength = captain.bonus_strength[1]
        if captain.bonus_health[0] in troops_unit.type:
            captain_bonus_health = captain.bonus_health[1]

        # Check if any type in monster[0].type matches any bonus type in troops[0].bonus
        self.troops_bonus = 0  # Default bonus value
        for bonus in troops_unit.bonus:
            if bonus[0] in monster_unit.type:  # Checking if bonus type applies to the monster type
                self.troops_bonus = bonus[1]  # Assign bonus value

        bonus_monster = 1 + self.monster_bonus
        bonus_troops_strength = 1 + self.bonus_strength + captain_bonus_strength + self.troops_bonus
        bonus_troops_health   = 1 + self.bonus_health   + captain_bonus_health
        # print(f'Bonus monster: {bonus_monster}')
        # print(f'Bonus troops health: {bonus_troops_health}')
        # print(f'Bonus troops strength: {bonus_troops_strength}')

        return bonus_monster, bonus_troops_strength, bonus_troops_health
    
    def hit(self, monster, troops, captain):
        bonus_monster, bonus_troops_strength, bonus_troops_health = self.bonus(monster, troops, captain)
        
        monster_strength = monster.strength * bonus_monster    
        monster_health   = monster.health   
        troops_strength  = troops.strength  * bonus_troops_strength
        troops_health    = troops.health    * bonus_troops_health
        
        monster_loss = round( troops_strength  * troops.amount   / monster_health  + 0.5 )
        troops_loss  = round( monster_strength * monster.amount  / troops_health   + 0.5 )
        troops_need  = round( monster_health   * monster.amount  / troops_strength + 0.5 )
        
        # print(f'damage from monster {monster_strength}')
        # print(f'damage needed to kill the monster {monster_health}')
        # troops_tot   = round(troops_loss + troops_kill)
        # print(f'monster strength: {monster_strength}')
        # print(f'monster health: {monster_health}')
        # print(f'troops strength: {troops_strength}')
        # print(f'troops amount: {troops.amount}')
        # print(f'monsters amount: {monster.amount}')
        # print(f'troops loss: {troops_loss}')
        # print(f'troops needed to kill the monster: {troops_kill}')
        # print(f'troops to be sent: {troops_tot}')
        return monster_loss, troops_loss, troops_need
    
    def round(self):

        captain = self.captain
        troops_have_hitten = [False]*len(self.troops)
        monster_have_hitten = [False]*len(self.monster.units)
        ihit_troops = 0
        ihit_monster = 0

        for ihit in range(max(len(self.troops), len(self.monster.units))):

            print(f'Hit: {ihit+1}')
            print(f'[units amount: {[unit.amount for unit in self.monster.units]}]')
            if all(unit.amount == 0 for unit in self.monster.units):
                break
            # Monster attack
            self.round_order()
            if ihit < len(self.monster_order):
                #Find strongest monster who has not attacked yet
                for monster_index_max in self.monster_order:
                    if monster_have_hitten[monster_index_max] == False and self.monster.units[monster_index_max].amount > 0:
                        break
                monster = self.monster.units[monster_index_max]

                if monster.amount > 0:
                    #Monster will attack fisrt the troops army they have a bonus for
                    bonus_monster = [0]*len(self.troops)
                    for itroops in self.troops_order:
                        bonus_monster[itroops], _, _ = self.bonus(monster, self.troops[itroops], captain)
                    #Trying to get the troops with the highest bonus
                    if ihit ==0 and self.troops[self.troops_order[bonus_monster.index(max(bonus_monster))]].amount == 0:
                        bonus_troops = [0]*len(self.troops)
                        for itroops in self.troops_order:
                            _, bonus_troops[itroops], _ = self.bonus(monster, self.troops[itroops], captain)
                        troops_index = self.troops_order[bonus_troops.index(max(bonus_troops))]
                        bonus_monster[troops_index] += 0.001

                    troops_index = self.troops_order[bonus_monster.index(max(bonus_monster))]
                    troops  = self.troops[troops_index]
                    _, max_troops_loss, _ = self.hit(monster, troops, captain)
                    
                    if self.troops[troops_index].amount > 0:
                        max_troops_loss = min(max_troops_loss, self.troops[troops_index].amount)
                        self.troops[troops_index].amount -= max_troops_loss
                    else:
                        self.troops_needed[troops_index] += max_troops_loss
                    print(f'monster {monster.__class__.__name__} kills {max_troops_loss} troops of type {self.troops[troops_index].__class__.__name__} level {self.troops[troops_index].level}')


            # Troops attack
            self.round_order()
            if ihit < len(self.troops_order):
                troops_index = self.troops_order[ihit]
                troops = self.troops[troops_index]

                # Find the monster with the highest order and non-zero amount
                for monster_index_max in self.monster_order:
                    if self.monster.units[monster_index_max].amount > 0:
                        break
                monster = self.monster.units[monster_index_max]

                if troops.amount > 0:
                    monster_loss, _, _ = self.hit(monster, troops, captain)
                    max_monster_loos = min(monster_loss, monster.amount)
                    monster.amount -= max_monster_loos
                    troops_have_hitten[troops_index] = True
                    print(f'troops {troops.__class__.__name__} level {troops.level} kills {max_monster_loos} monsters of type {monster.__class__.__name__}')
                else:
                    bonus_troops = [0]*len(self.troops)
                    for itroops in self.troops_order:
                        if troops_have_hitten[itroops]:
                            bonus_troops[itroops] = 0
                        else:
                            _, bonus_troops[itroops], _ = self.bonus(monster, self.troops[itroops], captain)
                    troops_index = self.troops_order[bonus_troops.index(max(bonus_troops))]
                    troops  = self.troops[troops_index]
                    _, _, min_troops_kill = self.hit(monster, troops, captain)
                    
                    self.troops_needed[troops_index] += min_troops_kill
                    self.monster.units[monster_index_max].amount = 0
                    troops_have_hitten[troops_index] = True
                    print(f'You need to send {min_troops_kill} troops of type {self.troops[troops_index].__class__.__name__} level {self.troops[troops_index].level} to kill the monster {monster.__class__.__name__}')

                self.strongest_troops[ihit] = troops_index
           
        
        # monster_loss, troops_loss, troops_kill = self.hit(self.monster.units[0], self.troops[0])
        # self.monster.units[0].amount -= monster_loss
        # self.troops[0].amount -= troops_loss
        # print(f'Monster: {[[i.__class__.__name__, i.amount]          for i in self.monster.units ]}')
        # print(f'Troops:  {[[i.__class__.__name__, i.level, i.amount] for i in self.troops ]}')
        # print(f'Monster loss: {monster_loss}')
        # print(f'Troops loss: {troops_loss}')



    def attack(self):
        iround = 0
        self.strongest_troops = [0]*len(self.troops)
        while True:
            if any(unit.amount > 0 for unit in self.monster.units):
                iround += 1
                print(f'Round {iround}')
                self.round()
            else:
                print(f'You have killed the monster!\n\n')        
                break

        # Calculate the troops needed to kill the monster so that the troops with the highest strength are sent first
        print(f'Strongest troops: {[self.troops[i].__class__.__name__ for i in self.strongest_troops]}')
        self.strongest_troops.reverse()
        print(f'Troops needed: {self.troops_needed}')
        min_strength = self.troops[self.strongest_troops[0]].strength * self.troops_needed[self.strongest_troops[0]]  
        for i in self.strongest_troops:
            strength_i = self.troops[i].strength * self.troops_needed[i]
            print(f'min_strength: {min_strength}, strength_i: {strength_i}')
            if strength_i < min_strength:
                self.troops_needed[i] += round((min_strength-strength_i) / self.troops[i].strength)+10
                min_strength = self.troops[i].strength * self.troops_needed[i]                  
                print(f'Troops needed: {self.troops_needed}')
                

        print(f'\nTroops needed:')
        for i in range(len(self.troops_needed)):
                if self.troops_needed[i] > 0:
                    print(f'{self.troops[i].__class__.__name__}: {self.troops_needed[i]}')        

       
# %%

bonus_health = 0.72
bonus_strength = 0.905
monster = m.Monsters.Elf(11)
troops = [a.Army.Spearman(3), a.Army.Rider(3)]
captain = c.Captains.Aydae(10)
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()

# %%
""" 
monster = m.Monsters.Barbarian(12)
troops = [a.Army.Rider(3), a.Army.Spearman(3), a.Army.Archers(3)]
captain = c.Captains.Aydae(5)

# monster = Monsters.Cursed().common_8
# troops = [Army.Archers(3)]
# captain = Captains.Minamoto(5)

attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()

monster = m.Monsters.Barbarian(12)
troops = [a.Army.Rider(3)]
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()
monster = m.Monsters.Barbarian(12)
troops = [a.Army.Spearman(3)]
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()
monster = m.Monsters.Barbarian(12)
troops = [a.Army.Archers(3)]
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()
monster = m.Monsters.Barbarian(12)
troops = [a.Army.Spearman(3,1284), a.Army.Archers(3,810)]
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()
monster = m.Monsters.Barbarian(12)
troops = [a.Army.Spearman(3,1284), a.Army.Archers(3,2000)]
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()
"""