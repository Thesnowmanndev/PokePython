from settings import *
from os.path import join

# pip install pytmx
from pytmx.util_pygame import load_pygame

from groups import AllSprites
from sprites import Sprite
from entities import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('PokePython')
        self.clock = pygame.time.Clock()
        
        # groups
        self.all_sprites = AllSprites()
        
        self.import_assets()
        self.setup(self.tmx_maps['world'], 'house')
    
    def import_assets(self):
        self.tmx_maps = {'world': load_pygame(join('data', 'maps', 'world.tmx'))}
    
    def setup(self, tmx_map, player_start_pos):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, self.all_sprites)
            
        for obj in tmx_map.get_layer_by_name('Entities'):
            if obj.name == 'Player' and obj.properties['pos'] == player_start_pos:
                self.player = Player((obj.x, obj.y), self.all_sprites)
    
    def run(self):
        while True:
            # track framerate 
            # https://www.youtube.com/watch?v=rWtfClpWSb8 - Understand Framerate & DeltaTime
            dt = self.clock.tick() / 1000
            
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # game logic
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()
            
if __name__ == '__main__':
    game = Game()
    game.run()