import pygame
from tank import Tank
from projectile import Projectile

class Seeker(Tank):
    def __init__(self, x, y, combat_x, combat_y) -> None:
        Tank.__init__(self, x, y)
        self.source_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("src/assets/Green_Tank_Sprite.png").convert_alpha(), (40, 70)),180)
        self.image = self.source_img
        self.source_rect = self.source_img.get_rect(x = self.x, y = self.y)
        self.rect = self.image.get_rect(x = self.x, y = self.y)
        self.rotation = 0
        self.combat_range = pygame.Rect(self.rect.x - combat_x, self.rect.y - combat_y, combat_x * 2 + 24, combat_y * 2 + 27)
        self.time_since_last_shot = 0
        self.seeker_rotation = 0
        self.seeker_group = pygame.sprite.Group()
        self.time_since_last_seeker = -50

    def tank_shoot(self, player):
        if len(self.seeker_group) < 10 and pygame.time.get_ticks() - self.time_since_last_seeker > 50:
            self.seeker_rotation += 50
            new_seeker = Projectile(self.source_rect.center[0], self.source_rect.center[1], self.seeker_rotation)
            self.seeker_group.add(new_seeker)

        for seeker in self.seeker_group:
            #deletes bullet that hits self first
            if self.rect.colliderect(seeker.rect) and pygame.time.get_ticks() - seeker.time_of_creation > 150:
                seeker.kill()
            #shoots new bullet if seeker hits tank
            elif player.rect.colliderect(seeker.rect):
                #calculates ahgle for shot
                self.rotation = seeker.rotation
                #rotates tank toward shot
                self.image = pygame.transform.rotate(self.source_img, self.rotation + 180)
                self.rect = self.image.get_rect()
                self.rect.center = self.source_rect.center
                if pygame.time.get_ticks() - self.time_since_last_shot > 1000:
                    self.time_since_last_shot = pygame.time.get_ticks()
                    super().tank_shoot()
                #cleans seeker bullet
                seeker.kill()