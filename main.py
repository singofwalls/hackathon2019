from random import randint
from weapons import dagger, longSword, scimitar, blackWand, greatSword, Weapon
from leveling import health, strength, accuracy

class Character:
    def __init__(self):
        self.name = ""
        self.healthMax = 1
        self.health = health + self.leveling.health
        self.strength = None
        self.weapon = None
        self.accuracy = accuracy + self.leveling.accuracy

    def attack(self, enemy):
        if not isinstance(self.weapon, type(None)):
            self.strength = strength
        else:
            self.strength = strength + self.weapon.strengthBonus

        damage = strength
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