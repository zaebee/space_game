import pygame
import weapon

class Player(pygame.sprite.Sprite):
    speed = 10
    
    def __init__(self, x=0, y=0, filename=None):
        super().__init__()
        self.x = x
        self.y = y
        self.bullets = pygame.sprite.Group()
        self.image = pygame.image.load(filename or 'images/player.png')
    
    def on_event(self, event):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                self.shoot()
        if keys[pygame.K_w]:
            self.moveUp()
        if keys[pygame.K_s]:
            self.moveDown()
        if keys[pygame.K_a]:
            self.moveLeft()
        if keys[pygame.K_d]:
            self.moveRight()
            
    def moveRight(self):
        self.x += self.speed
    
    def moveLeft(self):
        self.x -= self.speed
    
    def moveUp(self):
        self.y -= self.speed
    
    def moveDown(self):
        self.y += self.speed
        
    def shoot(self):
        # TODO: spawn laser
        rect = self.image.get_rect()
        laser = weapon.Laser(self.x + rect.centerx, self.y - rect.centery)
        self.bullets.add(laser)