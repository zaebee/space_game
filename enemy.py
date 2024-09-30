import random
import pygame

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, filename=None):
        super().__init__()
        # TODO: avoid to use magic numbers
        self.speed = random.randrange(2, 10)
        self.image = pygame.image.load(filename or 'images/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1024)
        self.rect.y = random.randrange(0, 768 // 3)
    
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed // 2
    
    def on_event(self, event):
        pass