import pygame
from missel import Missel

class Tank(pygame.sprite.Sprite):
    #list of all active bullets on the map
    total_missel_group = pygame.sprite.Group()
    def __init__(self, img, x, y,) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.source_img = pygame.transform.scale(img, (40, 70))
        self.image = pygame.transform.scale(img, (40, 70))
        self.x = x
        self.y = y
        self.source_rect = self.source_img.get_rect(center=(500, 500))
        self.rect = self.image.get_rect(center=(500, 500))
        self.rotation = 0
        self.missel_group = pygame.sprite.Group()

    def rotate_tank(self, rotation_value, barrier_group = []):
        print(self.rotation , "pre")
        self.rotation += rotation_value
        self.image = pygame.transform.rotate(self.source_img, self.rotation)
        self.rect = self.image.get_rect(center = self.source_rect.center)
        self.mask = pygame.mask.from_surface(self.image)
        if pygame.sprite.spritecollide(self, barrier_group, False, pygame.sprite.collide_mask):
            self.rotation -= rotation_value 
            self.image = pygame.transform.rotate(self.source_img, self.rotation)
            self.rect = self.image.get_rect(center = self.source_rect.center)
            print(self.rotation , "collide")
    
    

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
 
    #handles shooting for tanks
    def tank_shoot(self):
        if len(self.missel_group) < 4:
            new_projectile = Missel(self.source_rect.center[0], self.source_rect.center[1], self.rotation)
            self.missel_group.add(new_projectile)
            Tank.total_missel_group.add(new_projectile)

    #handles collision with bullets
    def tank_hit(self):
        from game import Game
        from enemy import Enemy
        for missel in Tank.total_missel_group:
            if pygame.time.get_ticks() - missel.time_of_creation > 150:
                if self.rect.colliderect(missel.rect):
                    self.kill()
                    missel.kill()
                    if isinstance(self, Enemy):
                        Game.enemy_count -= 1
        
