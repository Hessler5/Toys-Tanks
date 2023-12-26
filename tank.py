import pygame
from missel import Missel

class Tank:
    def __init__(self, img, x, y,) -> None:
        self.source_img = pygame.transform.scale(img, (40, 70))
        self.rotated_img = pygame.transform.scale(img, (40, 70))
        self.x = x
        self.y = y
        self.source_rect = self.source_img.get_rect(center=(50, 50))
        self.rotated_rect = self.rotated_img.get_rect(center=(50, 50))
        self.rotation = 0
        self.projectiles = []

    def rotate_tank(self, rotation_value):
        self.rotation += rotation_value
        self.rotated_img = pygame.transform.rotate(self.source_img, self.rotation)
        self.rotated_rect = self.rotated_img.get_rect(center = self.source_rect.center)

    def move_tank(self, velocity):
        forward_vector = pygame.Vector2(0, velocity).rotate(-self.rotation)
        self.source_rect.center += forward_vector
        self.rotated_rect.center += forward_vector

    def tank_shoot(self):
        new_projectile = Missel(self.source_rect.center[0] - 4, self.source_rect.center[1] - 4, self.rotation)
        self.projectiles.append(new_projectile)