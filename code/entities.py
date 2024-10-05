from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # image isnt accurate for the player atm
        self.image = pygame.Surface((100, 100))
        self.image.fill('red')
        self.rect = self.image.get_frect(center = pos)
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print('Up')
            
        if keys[pygame.K_DOWN]:
            print('Down')
            
        if keys[pygame.K_LEFT]:
            print('Left')
            
        if keys[pygame.K_RIGHT]:
            print('Right')
    
    def move(self, dt):
        pass
    
    def update(self):
        self.input()