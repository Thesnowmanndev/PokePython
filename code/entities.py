from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        # image isnt accurate for the player atm
        self.image = pygame.Surface((100, 100))
        self.image.fill('red')
        self.rect = self.image.get_frect(center = pos)