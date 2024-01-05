import pygame

class Health():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x + 37, y + 37, 25, 25)
