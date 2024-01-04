import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, rotation) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("src/assets/projectile.png").convert_alpha(), (18,18))
        self.rect = self.image.get_rect(center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.rotation = rotation
        self.reflections = 0
        self.missel_vector = pygame.Vector2(0, 10).rotate(-self.rotation)
        self.time_of_creation = pygame.time.get_ticks()

    def move_missel(self, barrier_group):
        #checks each barrier for collision
        for barrier in barrier_group:
            if self.rect.colliderect(barrier.rect):
                self.reflections += 1
                #reflects x 
                if barrier.rect.x < self.rect.center[0] < barrier.rect.x + barrier.rect.width:
                    self.missel_vector = pygame.Vector2(self.missel_vector[0], self.missel_vector[1] * -1)
                #reflects y
                elif barrier.rect.y < self.rect.center[1] < barrier.rect.y + barrier.rect.height:
                    self.missel_vector = pygame.Vector2(self.missel_vector[0] * -1, self.missel_vector[1])

            
        self.rect.center -= self.missel_vector
        #cleans projectile if time exceeds 5000 ticks
        if pygame.time.get_ticks() - self.time_of_creation > 5000:
            self.kill()
        #cleans projectile if reflections = 8   
        if self.reflections == 6:
            self.kill()

        
   
            



 