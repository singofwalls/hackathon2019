import pygame
import time
import random


class Entity:
    def __init__(self):

        self.speed = WALK_SPEED
        self.last_move = {}

        w, h = display.get_width(), display.get_height()

        self.rect = [random.randint(0, w - 10), random.randint(0, h - 10), 10, 10]
        self.color = (255, 125, 125)

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
        pygame.draw.rect(display, self.color, self.rect)


class Player(Entity):
    def __init__(self):
        super().__init__()
        self.speed = 0.6
        self.color = (125, 125, 255)

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

    def change_direction(self):
        if random.randint(0, 5) == 1 or isinstance(self.movement, type(None)):
            self.movement = [random.randint(-1, 1), random.randint(-1, 1)]

    def control(self):
        if self.last_direction_choice + DIRECTION_CHOICE_INTERVAL < time.time():
            self.last_direction_choice = time.time()
            self.change_direction()
        self.move(tuple(self.movement))


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


MOVE_TIME = 0.001
DIRECTION_CHOICE_INTERVAL = 0.1
WALK_SPEED = 0.5

display = pygame.display.set_mode([1000, 700], pygame.RESIZABLE)

entities = []

player = Player()

entities.append(player)
for i in range(0, 20):
    entities.append(NPC())


running = True

last_tick = time.time()

while running:

    time.sleep(0.000001)

    display.fill((0, 0, 0))

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode(event.dict["size"], pygame.RESIZABLE)

        elif event.type == pygame.QUIT:
            running = False

    if not running:
        break

    for entity in entities:
        entity.control()
        entity.render(display)

    pygame.display.flip()

pygame.display.quit()
