from settings import *
from os.path import join

# pip install pytmx
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('PokePython')
        
        self.import_assets()
    
    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('data', 'maps', 'world.tmx'))}
        
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
            pygame.display.update()
            
if __name__ == '__main__':
    game = Game()
    game.run()