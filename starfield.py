"""
Simple starfield program created with pygame
"""
import sys
import pygame
from pygame.locals import *
import random

pygame.init()

FPS = 60
EngineClock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("Starfield")

MIN_STAR_SIZE = 1
MAX_STAR_SIZE = 3

class Star(pygame.sprite.Sprite):
    def __init__(self, size): # size : the width & height in pixels
        super().__init__()

        self.image = pygame.Surface([size, size])
        self.image.fill(WHITE)

        self.speed = size * random.randint(1, 2)

        self.rect = self.image.get_rect()
        rand_coord_x = random.randint(0, SCREEN_WIDTH)
        rand_coord_y = random.randint(0, SCREEN_HEIGHT)
        self.rect.center = (rand_coord_x, rand_coord_y)
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > SCREEN_HEIGHT):
            self.rect.top = 0
            rand_coord_x = random.randint(0, SCREEN_WIDTH)
            self.rect.center = (rand_coord_x, 0)


stars = pygame.sprite.Group()
for i in range(200):
    star = Star(random.randint(MIN_STAR_SIZE, MAX_STAR_SIZE))
    stars.add(star)

# Core Update Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # wipe the previous screen before redrawing
    DISPLAYSURF.fill(BLACK)  
    
    for star in stars:
        DISPLAYSURF.blit(star.image, star.rect)
        star.move()

    pygame.display.update()
    EngineClock.tick(FPS)
