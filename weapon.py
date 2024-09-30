import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, filename=None):
        super().__init__()
        print(f'Spawn laser: {x, y}')
        self.speed = 10
        self.image = pygame.image.load(filename or 'images/laserGreen.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def update(self):
        self.rect.y -= self.speed
    
    def on_event(self, event):
        pass