import pygame
from barrier import Barrier

class Game:
    def __init__(self, screen, player) -> None:
        self.screen = screen
        self.player = player
        self.run = True
        self.barrier_group = pygame.sprite.Group()


    #handles key pushes
    def handle_events(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.player.rotate_tank(3)
        if pressed[pygame.K_d]:
            self.player.rotate_tank(-3)
        if pressed[pygame.K_w]:
            self.player.move_tank(-3, self.barrier_group)
        if pressed[pygame.K_s]:
            self.player.move_tank(3, self.barrier_group)

    #handles single button presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.tank_shoot()

    #moves missles every game loop
        for missel in self.player.projectiles:
            missel.move_missel()

    #drawing function
    def draw_window(self, player, world_data):
        self.screen.fill((220, 220, 220))


        #reads level data
        for row in range(len(world_data)):
            for column in range(len(world_data[row])):
                if world_data[row][column] == 1:
                    new_barrier = Barrier()
                    self.screen.blit(new_barrier.image, (column * 100, row * 100))
                    new_barrier.rect.x = column * 100
                    new_barrier.rect.y = row * 100
                    self.barrier_group.add(new_barrier)

        self.screen.blit(player.image, player.rect)
        for projectile in self.player.projectiles:
            self.screen.blit(projectile.source_surface, (projectile.x, projectile.y ))
        pygame.display.update()