from random import randint
from weapons import dagger, longSword, scimitar, blackWand, greatSword, Weapon, fist
from leveling import leveling


class Character:
    def __init__(self):
        self.name = "player"
        self.leveling = leveling()
        self.strength, self.health = self.leveling.currentLevelRewards(
            self.leveling.level
        )
        self.healthMax = self.health
        self.weapon = fist

    def attack(self, enemy):
        totalStrength = self.strength + self.weapon.strengthBonus
        damage = randint(0, int(self.weapon.maxHit(totalStrength)))
        damage *= (self.health / self.healthMax) * 1000

        print("Damage is " + str(damage))
        enemy.health = enemy.health - damage
        self.health += damage
        self.healthMax += damage

        if damage == 0:
            print("%s dodged %s's attack!" % (enemy.name, self.name))
        else:
            print("%s attacked %s!" % (self.name, enemy.name))

        return enemy.health <= 0


class Enemy(Character):
    def __init__(self, player):
        Character.__init__(self)
        self.name = "ENEMY"  # what should we name our enemy?
        self.health = randint(1, player.health)


# class Interactions:
#     def userNPC
