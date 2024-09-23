import pygame

class Player:
    x = 0
    y = 0
    speed = 2
    
    def __init__(self, filename=None):
        filename = filename or 'images/player.png'
        self.surface = pygame.image.load(filename)
    
    def moveRight(self):
        self.x += self.speed
    
    def moveLeft(self):
        self.x -= self.speed
    
    def moveUp(self):
        self.y -= self.speed
    
    def moveDown(self):
        self.y += self.speed
    
