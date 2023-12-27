import pygame
from missel import Missel

class Tank(pygame.sprite.Sprite):
    def __init__(self, img, x, y,) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.source_img = pygame.transform.scale(img, (40, 70))
        self.image = pygame.transform.scale(img, (40, 70))
        self.x = x
        self.y = y
        self.source_rect = self.source_img.get_rect(center=(500, 500))
        self.rect = self.image.get_rect(center=(500, 500))
        self.rotation = 0
        self.projectiles = []

    def rotate_tank(self, rotation_value):
        self.rotation += rotation_value
        self.image = pygame.transform.rotate(self.source_img, self.rotation)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center = self.source_rect.center)

    def move_tank(self, velocity, barrier_group):
        forward_vector = pygame.Vector2(0, velocity).rotate(-self.rotation)
        test_rect = self.rect.copy()
        test_rect.center += forward_vector
        collision = False
        self.source_rect.center += forward_vector
        self.rect.center += forward_vector
        if pygame.sprite.spritecollide(self, barrier_group, False, pygame.sprite.collide_mask):
            collision = True
        if collision == True:
            self.source_rect.center -= forward_vector
            self.rect.center -= forward_vector

    def tank_shoot(self):
        new_projectile = Missel(self.source_rect.center[0] - 4, self.source_rect.center[1] - 4, self.rotation)
        self.projectiles.append(new_projectile)