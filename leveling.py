from weapons import strengthBonus
class leveling:

    def xpToLevelUp(currentLevel): 
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

    def levelingUp(xpEarned, xpNeeded, currentLevel): 
        #if the amount of xp the user has earned is greater than the amount they need to level up, they advance one level
        if (xpEarned > xpNeeded):
            currentLevel += 1
        return currentLevel

    def currentLevelRewards(currentLevel):
        #determines the users current level and gives them attributes depending on their level
        health = 0
        strength = 0
        accuracy = 0

        if(currentLevel == 0):
            health = 5
            strength = 5
            accuracy = 5
        elif(currentLevel == 1):
            health = 10
            strength = 10
            accuracy = 10
        elif (currentLevel == 2):
            health = 20
            strength = 20
            accuracy = 20
        elif (currentLevel == 3):
            health = 30
            strength = 30
            accuracy = 30
        elif (currentLevel == 4):
            health = 40
            strength = 40
            accuracy = 40
        elif (currentLevel == 5):
            health = 50
            strength = 50
            accuracy = 50
            
        return strength
        return health 
        

    
