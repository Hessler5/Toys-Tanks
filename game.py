import pygame

class Game:
    def __init__(self, screen, player) -> None:
        self.screen = screen
        self.player = player
        self.run = True


    #handles key pushes
    def handle_events(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.player.rotate_tank(3)
        if pressed[pygame.K_d]:
            self.player.rotate_tank(-3)
        if pressed[pygame.K_w]:
            self.player.move_tank(-3)
        if pressed[pygame.K_s]:
            self.player.move_tank(3)

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
    def draw_window(self, player):
        self.screen.fill((80, 80, 80))
        self.screen.blit(player.rotated_img, player.rotated_rect)
        for projectile in self.player.projectiles:
            self.screen.blit(projectile.source_surface, (projectile.x, projectile.y ))
        pygame.display.update()