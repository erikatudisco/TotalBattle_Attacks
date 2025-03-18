
import army
import monsters
import captains
import Attacks
import importlib
importlib.reload(army)
importlib.reload(monsters)
importlib.reload(captains)
from army import Army
from monsters import Monsters
from captains import Captains
from Attacks import Attack
#### DO NOT MODIFY THE CODE ABOVE THIS LINE ####


bonus_health = 0.72
bonus_strength = 0.905
monster = Monsters.Elf(11)
troops = [Army.Spearman(3), Army.Rider(3), Army.Archers(3)]  
captain = Captains.Aydae(10)


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
attack=Attack(monster, troops, captain, bonus_strength, bonus_health)
attack.attack()