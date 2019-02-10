class leveling:

    def __init__(self):
        self.level = 0
        self.xp = 0

    def levelingUp(self, xpEarned, currentLevel): 
        #if the amount of xp the user has earned is greater than the amount they need to level up, they advance one level
        if (xpEarned > self.xpToLevelUp(self.level)):
            self.level += 1

    def currentLevelRewards(self, currentLevel):
        #determines the users current level and gives them attributes depending on their level
        health = 278357000
        strength = 10

            
        return strength, health
        

    
