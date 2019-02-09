import pygame
import time


class Entity:
    def __init__(self):

        self.speed = 1
        self.last_move = {}

        self.rect = [0, 0, 10, 10]
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
    def control(self):
        for key, pressed in enumerate(pygame.key.get_pressed()):
            if pressed and key in MOVEMENTS:
                self.move(MOVEMENTS[key])


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


entities = []

player = Player()

entities.append(player)

display = pygame.display.set_mode([500, 500], pygame.RESIZABLE)


running = True

last_tick = time.time()

while running:

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
        entity.render(display)

    player.control()

    pygame.display.flip()

pygame.display.quit()
