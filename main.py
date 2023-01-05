from random import random, randrange
from time import sleep

import pygame
from pygame.locals import *

from rocket import Rocket
from stars import Star

from saturn import Saturn

DISPLAY_SIZE = (1920, 1080)

STAR_SIZE = (20, 20)


def init():
    pygame.init()
    surface = pygame.display.set_mode(DISPLAY_SIZE)

    # star
    star = Star(40)
    star.draw(surface)


    rocket = Rocket()
    rocket_x = 10
    rocket_y = 10

    rocket.draw(rocket_x, rocket_y, surface)
    star.draw(surface)

    saturn = Saturn()
    saturn.draw(surface)

    pygame.display.flip()

    pygame.display.flip()

    running = True

    def redraw(x, y):
        transparent = (0, 0, 0, 0)
        surface.fill(transparent)
        rocket.draw(x, y, surface)
        star.draw(surface)
        saturn.draw(surface)
        pygame.display.flip()


    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    break
                elif event.key == K_UP:
                    rocket_y = rocket_y - 20
                    redraw(rocket_x, rocket_y)
                elif event.key == K_DOWN:
                    rocket_y = rocket_y + 20
                    redraw(rocket_x, rocket_y)
                elif event.key == K_LEFT:
                    rocket_x = rocket_x - 20
                    redraw(rocket_x, rocket_y)
                elif event.key == K_RIGHT:
                    rocket_x = rocket_x + 20
                    redraw(rocket_x, rocket_y)


if __name__ == '__main__':
    init()

# movement
