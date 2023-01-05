import pygame

SATURN_SIZE = (220, 190)


class Saturn:
    def __init__(self):
        saturn = pygame.image.load('resources/saturn.png').convert()
        self.saturn = pygame.transform.scale(saturn, SATURN_SIZE)

    def draw(self, surface):
        surface.blit(self.saturn, (300, 100))
