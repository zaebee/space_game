import pygame

import pygame.docs

class Game:
    WIDTH = 800
    HEIGHT = 600
    
    def __init__(self):
        print('Init game')
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Easy game')
    
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        
    def on_render(self):
        pass
    
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
