from Attacks import Attack
from army import Army
from monsters import Monsters
from captains import Captains
import importlib
importlib.reload(Army)
importlib.reload(Monsters)
importlib.reload(Captains)
#### DO NOT MODIFY THE CODE ABOVE THIS LINE ####


bonus_health = 0.72
bonus_strength = 0.905
monster = m.Monsters.Elf(11)
troops = [a.Army.Spearman(3), a.Army.Rider(3), a.Army.Archers(3)]  
captain = c.Captains.Aydae(10)


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()