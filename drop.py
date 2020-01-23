from random import randint
import pygame


class Drop(object):
    """
        Class for drop object
    """
    def __init__(self, screenWidth):
        self.width = randint(1,3)
        self.length = randint(20,50)
        self.yspeed = randint(4,10)
        self.x = randint(0, screenWidth-self.width)
        self.y = randint(-20, 20)  # start position
        self.color = (138,43,226)
    
    def fall(self):
        self.y += self.yspeed
    
    def show(self, screen):
        startPoint = (self.x, self.y)
        endPoint = (self.x, self.y + self.length)
        pygame.draw.line(screen, self.color, startPoint, endPoint, self.width)


if __name__ == '__main__':
    d1 = Drop(10, 10)
    print(d1.width)
    d1.width = 15
    print(d1.width)
    d1.show()