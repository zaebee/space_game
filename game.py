import pygame

import pygame.docs


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
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.CAPTION)
        self.init_images()
    
    def display_fps(self):
        caption = '{} - FPS: {:.2f}'.format(self.CAPTION, self.clock.get_fps())
        pygame.display.set_caption(caption)
    
    def init_images(self):
        bg_surface = pygame.image.load('images/kosmos.png')
        self.display.blit(bg_surface, bg_surface.get_rect())
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        
    def on_render(self):
        pass
    
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.display_fps()
            self.on_render()
            for event in pygame.event.get():
                self.on_event(event)
            pygame.display.flip()
        self.on_cleanup()
        
game = Game()
game.on_execute()
