import random
import pygame

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x=0, y=0, filename=None):
        super().__init__()
        print(f'init ufo [{y}, {y}]')
        self.x = x
        self.y = y
        self.speed = random.randrange(2, 10)
        self.image = pygame.image.load(filename or 'images/ufo.png')
        self.rect = self.image.get_rect()
    
    def update(self):
        self.y += self.speed
        self.x += self.speed // 2
    
    def on_event(self, event):
        pass