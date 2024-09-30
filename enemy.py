import random
import pygame

# TODO: avoid to use magic numbers. Create settings.py
WIDTH = 1024
HEIGHT = 758
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, filename=None):
        super().__init__()
        # TODO: avoid to use magic numbers
        self.speed = random.randrange(2, 10)
        self.image = pygame.image.load(filename or 'images/ufo.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = random.randrange(0, 40)
    
    def update(self):
        self.rect.y += self.speed
        self.rect.x += self.speed // 2
        out_of_screen = any([
           self.rect.top > HEIGHT,
           self.rect.left < 0,
           self.rect.right > WIDTH
        ])
        if out_of_screen:
            self.rect.x = random.randrange(0, WIDTH)
            self.rect.y = random.randrange(0, 40)
    
    def on_event(self, event):
        pass