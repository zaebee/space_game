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
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.CAPTION)
        self.init_images()
        self.hero = player.Player(400, 400)
    
    def display_fps(self):
        caption = '{} - FPS: {:.2f}'.format(self.CAPTION, self.clock.get_fps())
        pygame.display.set_caption(caption)
    
    def init_images(self):
        bg_surface = pygame.image.load('images/kosmos.png')
        self.screen.blit(bg_surface, bg_surface.get_rect())
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        self.hero.on_event(event)
        
    def on_render(self):
        self.screen.blit(
            self.hero.surface, (self.hero.x, self.hero.y))
    
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.display_fps()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
            pygame.display.flip()
        self.on_cleanup()
        
game = Game()
game.on_execute()
