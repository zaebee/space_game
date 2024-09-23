import pygame

class Player:
    speed = 2
    
    def __init__(self, x=0, y=0, filename=None):
        self.x = x
        self.y = y
        filename = filename or 'images/player.png'
        self.surface = pygame.image.load(filename)
    
    def on_event(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hero.moveUp()
        if keys[pygame.K_s]:
            self.hero.moveDown()
        if keys[pygame.K_a]:
            self.hero.moveLeft()
        if keys[pygame.K_d]:
            self.hero.moveRight()
            
    def moveRight(self):
        self.x += self.speed
    
    def moveLeft(self):
        self.x -= self.speed
    
    def moveUp(self):
        self.y -= self.speed
    
    def moveDown(self):
        self.y += self.speed