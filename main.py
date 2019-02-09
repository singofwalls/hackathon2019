from random import randint
from weapons import dagger, longSword, scimitar, blackWand, greatSword, Weapon
from leveling import health, strength

class Character:
    def __init__(self):
        self.name = ""
        self.healthMax = 1
        self.health = health + self.leveling.health
        self.strength = strength
        self.weapon = Weapon # how do we know which weapon is being held & used?

    def attack(self, enemy):
        damage = min(max(randint(0, self.health) - randint(0, enemy.health), 0), enemy.health)
        

        if self.weapon == dagger:
            self.strength = strength + self.weapon.strengthBonus
        elif self.weapon == longSword:
            



        enemy.health = enemy.health - damage

        if damage == 0:
            print("%s dodged %s's attack!" % (enemy.name, self.name))
        else:
            print("%s attacked %s!" % (self.name, enemy.name))
        return enemy.health <= 0
            

class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = "ENEMY" #what should we name our enemy?
        self.health = randint(1, player.health)

