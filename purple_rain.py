import pygame
import sys
from drop import Drop
from time import sleep
from random import randint


def init_drop_objects(screenWidth, number=300):
    drops = []
    for i in range(number):
        newDrop = Drop(screenWidth)
        drops.append(newDrop)
    return drops

def update_drop_objects(drops, screen):
    """
        pass drops by reference
    """
    for drop in drops:
        if drop.y > screen.get_height():
            drop.y = randint(-20, 20)
        drop.fall()
        drop.show(screen)


def catch_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def init_settings(screenWidth=900, screenLength=600):
    # set the size of screen
    screen = pygame.display.set_mode((screenWidth,screenLength))
    # set the title of the screen
    pygame.display.set_caption("purple rain")
    return screen


def main():
    screenWidth, screenLength = 900, 600
    screen = init_settings(screenWidth, screenLength)
    drops = init_drop_objects(screen.get_width())
    while True:
        catch_exit()
        screen.fill((230, 230, 250))
        update_drop_objects(drops, screen)
        pygame.display.flip()
if __name__ == '__main__':
    main()