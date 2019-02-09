import pygame
import time
import random
import json

from characters import Character


pygame.init()


class Entity:
    def __init__(self):

        self.speed = WALK_SPEED
        self.last_move = {}

        w, h = display.get_width(), display.get_height()

        self.rect = [
            random.randint(0, w - WIDTH),
            random.randint(0, h - WIDTH),
            WIDTH,
            WIDTH,
        ]
        self.surface = pygame.Surface(self.rect[2:], pygame.SRCALPHA, 32)
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(PLAYER_IMAGE, (0, 0))

        self.character = Character()

        self.attack_time = 0

    def attack(self, entity):
        if self.attack_time + ATTACK_INTERVAL < time.time():
            self.attack_time = time.time()
            return self.character.attack(entity.character)
        return None

    def move(self, displacement_rect):
        if (
            displacement_rect not in self.last_move
            or time.time() > self.last_move[displacement_rect] + MOVE_TIME
        ):
            for ind, value in enumerate(displacement_rect):
                self.rect[ind] += value * self.speed
            self.last_move[displacement_rect] = time.time()
        self.check_bounds()

    def check_bounds(self):
        w, h = display.get_width(), display.get_height()
        self.rect[0] = min(max(0, self.rect[0]), w - self.rect[2])
        self.rect[1] = min(max(0, self.rect[1]), h - self.rect[3])

    def render(self, display):
        display.blit(self.surface, self.rect)
        health = max((self.character.health / self.character.healthMax) * 100, 0)
        for cutoff in HEALTH_COLORS:
            if cutoff <= health:
                color = HEALTH_COLORS[cutoff]
                break

        rect = self.rect[:2] + [int(self.rect[2] * health / 100), self.rect[3] / 5]
        rect[1] -= rect[3]
        pygame.draw.rect(display, color, rect)

        label = FONT.render(str(round(self.character.health, 0)), False, (0, 0, 0))
        display.blit(label, (self.rect[0], self.rect[1] - 10))

        color = (255, 255, 255)
        if isinstance(self, Player):
            color = (125, 255, 125)
        label = FONT.render(str(self.character.name), False, color)
        display.blit(label, (self.rect[0], self.rect[1] + self.rect[3]))



    def collide(self, entity):
        ax1 = self.rect[0]
        ay1 = self.rect[1]
        ax2 = ax1 + self.rect[2]
        ay2 = ay1 + self.rect[3]

        bx1 = entity.rect[0]
        by1 = entity.rect[1]
        bx2 = bx1 + entity.rect[2]
        by2 = by1 + entity.rect[3]

        return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.speed = WALK_SPEED * 1.1

    def control(self):
        for key, pressed in enumerate(pygame.key.get_pressed()):
            if pressed and key in MOVEMENTS:
                self.move(MOVEMENTS[key])


class NPC(Entity):
    def __init__(self):
        super().__init__()
        self.movement = None
        self.last_direction_choice = time.time()

        self.change_direction()
        self.character.name = "Man"

    def change_direction(self):
        if random.randint(0, 5) == 1 or isinstance(self.movement, type(None)):
            self.movement = [random.randint(-1, 1), random.randint(-1, 1)]

    def control(self):
        if self.last_direction_choice + DIRECTION_CHOICE_INTERVAL < time.time():
            self.last_direction_choice = time.time()
            self.change_direction()
        self.move(tuple(self.movement))


def reset_background(size):
    global display, background_surface, BACKGROUND_IMAGE

    display = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("World War Simulator")

    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, size)

    background = pygame.Surface(size)
    background_surface = pygame.Surface(size)
    background_surface.fill((0, 0, 0, 0))
    background_surface.blit(BACKGROUND_IMAGE, (0, 0, *size))


def add_players():
    for i in range(0, 10):
        npc = NPC()
        country = random.choice(pops)
        while not country["population"] or country["country"] in destroyed:
            country = random.choice(pops)
        npc.character.health = int(country["population"])
        npc.character.healthMax = int(country["population"])
        npc.character.name = country["country"]
        entities.append(npc)


# Obtained json from https://github.com/samayo/country-json/blob/master/src/country-by-population.json
with open("populations.json") as f:
    pops = json.load(f)

MOVEMENTS = {
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_a: (-1, 0),
    pygame.K_d: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
}

HEALTH_COLORS = {
    75: (0, 255, 0),
    50: (207, 221, 51),
    25: (239, 184, 45),
    0: (255, 0, 0),
}

WIDTH = 50
DEFAULT_SIZE = [1000, 700]
display = pygame.display.set_mode(DEFAULT_SIZE, pygame.RESIZABLE)

BACKGROUND_IMAGE = pygame.image.load("assets/grass.png")
PLAYER_IMAGE = pygame.image.load("assets/player.png")
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (WIDTH, WIDTH))

PLAYER_IMAGE.convert_alpha()
BACKGROUND_IMAGE.convert_alpha()
background_surface = None
reset_background(DEFAULT_SIZE)


MOVE_TIME = 0.001
DIRECTION_CHOICE_INTERVAL = 0.1
WALK_SPEED = 0.7
ATTACK_INTERVAL = .01

FONT = pygame.font.SysFont('Arial', 10)

entities = []

player = Player()

entities.append(player)

running = True

destroyed = []

add_players()

while running:

    time.sleep(0.000001)

    display.blit(background_surface, (0, 0))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.VIDEORESIZE:
            reset_background(event.dict["size"])

        elif event.type == pygame.QUIT:
            running = False

    if not running:
        break

    for entity in entities:
        if entity.character.name in destroyed:
            continue
        entity.control()
        entity.render(display)

    for entity in entities:
        if entity.character.name in destroyed:
            continue
        for entity2 in entities:
            if entity2.character.name in destroyed:
                continue
            if entity is not entity2 and entity.collide(entity2):
                if entity.attack(entity2):
                    destroyed.append(entity2.character.name)

    if len(entities) - len(destroyed) <= 1:
        add_players()

    pygame.display.flip()

pygame.display.quit()
