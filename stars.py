# rocket
from random import randrange

import pygame

STAR_SIZE = (20, 20)


class Star:
    def __init__(self, count):
        star = pygame.image.load('resources/star.png').convert()
        self.star = pygame.transform.scale(star, STAR_SIZE)
        self.coordinates = []
        for i in range(count):
            x = randrange(1920)
            y = randrange(1080)
            self.coordinates.append((x, y))

    def draw(self, surface):
        for x, y in self.coordinates:
            surface.blit(self.star, (x, y))
