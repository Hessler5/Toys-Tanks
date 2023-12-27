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

    def rotate_tank(self, rotation_value, barrier_group):
        collision = False
        self.rotation += rotation_value 
        self.image = pygame.transform.rotate(self.source_img, self.rotation)
        self.rect = self.image.get_rect(center = self.source_rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        if pygame.sprite.spritecollide(self, barrier_group, False, pygame.sprite.collide_mask):
            collision = True
        if collision == True:
            self.rotation -= rotation_value 
            self.image = pygame.transform.rotate(self.source_img, self.rotation)
            self.rect = self.image.get_rect(center = self.source_rect.center)
    

    def move_tank(self, velocity, barrier_group):
        forward_vector = pygame.Vector2(0, velocity).rotate(-self.rotation)
        y_vector = pygame.Vector2(0, forward_vector[1])
        x_vector = pygame.Vector2(forward_vector[0], 0)

        #checks for collision in the x direction
        self.source_rect.center += y_vector 
        self.rect.center += y_vector 
        Y_collision = False
        if pygame.sprite.spritecollide(self, barrier_group, False, pygame.sprite.collide_mask):
            Y_collision = True
        if Y_collision == True:
            self.source_rect.center -= y_vector 
            self.rect.center -= y_vector 


        #checks for collision in the x direction
        self.source_rect.center += x_vector 
        self.rect.center += x_vector 
        X_collision = False
        if pygame.sprite.spritecollide(self, barrier_group, False, pygame.sprite.collide_mask):
            X_collision = True
        if X_collision == True:
            self.source_rect.center -= x_vector 
            self.rect.center -= x_vector 
 

    def tank_shoot(self):
        new_projectile = Missel(self.source_rect.center[0] - 4, self.source_rect.center[1] - 4, self.rotation)
        self.projectiles.append(new_projectile)