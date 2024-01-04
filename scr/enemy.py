import pygame
from tank import Tank

class Enemy(Tank):
    def __init__(self, x, y, combat_x, combat_y) -> None:
        Tank.__init__(self, x, y)
        self.source_img = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("assets/Blue_Tank_Sprite.png").convert_alpha(), (40, 70)),180)
        self.image = self.source_img
        self.source_rect = self.source_img.get_rect(x = self.x, y = self.y)
        self.rect = self.image.get_rect(x = self.x, y = self.y)
        self.rotation = 0
        self.combat_range = pygame.Rect(self.rect.x - combat_x, self.rect.y - combat_y, combat_x * 2 + 24, combat_y * 2 + 27)
        self.time_since_last_shot = 0

    #shoots toward player upon collision with combat range
    def tank_shoot(self, player):
        if self.combat_range.colliderect(player.rect): 
            v1 = pygame.Vector2(0, 0)
            v2 = pygame.Vector2(player.source_rect.center[0] - self.source_rect.center[0], player.source_rect.center[1]-self.source_rect.center[1])
            #calculates ahgle for shot
            angle_v1_v2_degree = v1.angle_to(v2)
            self.rotation = - angle_v1_v2_degree - 90
            #rotates tank toward shot
            self.image = pygame.transform.rotate(self.source_img, self.rotation + 180)
            self.rect = self.image.get_rect()
            self.rect.center = self.source_rect.center
            if pygame.time.get_ticks() - self.time_since_last_shot > 1000:
                self.time_since_last_shot = pygame.time.get_ticks()
                super().tank_shoot()


