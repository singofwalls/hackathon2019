from random import randint
from weapons import dagger, longSword, scimitar, blackWand, greatSword, maxHit, accuracyBonus, Weapon
from leveling import health, strength, accuracy

class Character:
    def __init__(self):
        self.name = ""
        self.healthMax = 1
        self.health = health + self.leveling.health
        self.totalStrength = None
        self.weapon = None
        self.totalAccuracy = accuracy + self.leveling.accuracy
        willHit = False

        if totalAccuracy > 

    def attack(self, enemy):
        if not isinstance(self.weapon, type(None)):
            self.totalStrength = strength
        else:
            self.totalStrength = strength + self.weapon.strengthBonus

        damage = randint(0, maxHit)
        print("Damage is " + damage)
        enemy.health = enemy.health - damage

        if damage == 0:
            print("%s dodged %s's attack!" % (enemy.name, self.name))
        else:
            if willHit == True:
                print("%s attacked %s!" % (self.name, enemy.name))
            else:

        return enemy.health <= 0

class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = "ENEMY" #what should we name our enemy?
        self.health = randint(1, player.health)