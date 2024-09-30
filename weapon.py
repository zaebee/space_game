import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, filename=None):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 10
        self.image = pygame.image.load(filename or 'images/laserGreen.png')
    
    def update(self):
        self.y -= self.speed
    
    def on_event(self, event):
        pass