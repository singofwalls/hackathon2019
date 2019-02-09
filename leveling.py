
class leveling:

    def __init__(self):
        self.level = 0
        self.xp = 0


    def xpToLevelUp(self, currentLevel): 
        #takes the users current level to determine how much xp they need to get to the next level
        xpEarned = 0
        for x in range(1, currentLevel + 1): 
            xpNeeded = (5*x*2**(x/7))
        return xpNeeded
        #xp needed for level 1: 5.52045
        #xp needed for level 2: 12.19014
        #xp needed for level 3: 20.18850
        #xp needed for level 4: 29.71989
        #xp needed for level 5: 41.01677

    def levelingUp(self, xpEarned, currentLevel): 
        #if the amount of xp the user has earned is greater than the amount they need to level up, they advance one level
        if (xpEarned > self.xpToLevelUp(self.level)):
            self.level += 1

    def currentLevelRewards(self, currentLevel):
        #determines the users current level and gives them attributes depending on their level
        health = 278357000
        strength = 10

            
        return strength, health
        

    
