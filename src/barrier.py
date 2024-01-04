import pygame

class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("src/assets/barrier.png").convert(), (100, 100))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(x = self.x, y = self.y)
        self.mask = pygame.mask.from_surface(self.image)

