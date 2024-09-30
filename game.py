import pygame

import player


class Game:
    CAPTION = 'Easy game'
    WIDTH = 800
    HEIGHT = 600
    FPS = 60
    
    def __init__(self):
        print('Init game')
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load('images/kosmos.png')
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.hero = player.Player(400, 400)
    
    def display_fps(self):
        caption = '{} - FPS: {:.2f}'.format(self.CAPTION, self.clock.get_fps())
        pygame.display.set_caption(caption)
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        self.hero.on_event(event)
        
    def on_render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, self.bg.get_rect())
        self.screen.blit(
            self.hero.image, (self.hero.x, self.hero.y))
        self.display_fps()
        self.clock.tick(self.FPS)
        pygame.display.flip()
    
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        while self.running:
            self.on_render()
            for event in pygame.event.get():
                self.on_event(event)
        self.on_cleanup()
        
game = Game()
game.on_execute()
