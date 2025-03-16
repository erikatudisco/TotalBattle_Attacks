class Captains:

    class Aydae:
        def __init__(self, level) -> None:
            self.level = level
            self.bonus_health = ['Guardsman', self.level/100]
            self.bonus_strength = ['Guardsman', self.level/100]

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