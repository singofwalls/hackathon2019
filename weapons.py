
class Weapon:
    def __init__(self, name, strengthBonus):
        self.name = name
        self.strengthBonus = strengthBonus


    def maxHit(self, totalStrength):
        return totalStrength * 100
        
 
fist = Weapon("Fist", 0)
dagger = Weapon("Dagger", 1)
longSword = Weapon("Long Sword", 3)
scimitar = Weapon("Scimitar", 5)
blackWand = Weapon("Black Wand", 7)
greatSword = Weapon("Great Sword", 10)

        
