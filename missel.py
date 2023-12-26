import pygame

class Missel:
    def __init__(self, x, y, rotation) -> None:
        self.x = x
        self.y = y
        self.source_surface = pygame.Surface((12, 12), pygame.SRCALPHA)
        self.source_img = pygame.draw.circle(self.source_surface, (255,255,255), (self.source_surface.get_width()//2,self.source_surface.get_height()//2), 4)
        self.rotation = rotation

    def move_missel(self):
        missel_vector = pygame.Vector2(0, 10).rotate(-self.rotation)
        self.x -= missel_vector[0]
        self.y -= missel_vector[1]





 