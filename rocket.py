# rocket
import pygame

ROCKET_SIZE = (90, 90)


class Rocket:
    def __init__(self):
        rocket = pygame.image.load('resources/rocket.png').convert()
        self.rocket = pygame.transform.scale(rocket, ROCKET_SIZE)

    def draw(self, x, y, surface):
        surface.blit(self.rocket, (x, y))


if __name__ == '__main__':
    rrrr = Rocket()
    rrrr.draw(1, 2, 4)
