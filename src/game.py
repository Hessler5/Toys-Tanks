import pygame
from barrier import Barrier
from tank import Tank
from enemy import Enemy
from text import Text
from trishot_enemy import Trishot
from seeker_enemy import Seeker

class Game:
    #varriable to make quit button accessable by main file
    quit_game = False
    #total count of enemies to determin when level finish should appear
    enemy_count= 0 
    #total player lives counter
    lives = 3
    #tells main loop to respwan player
    respawn = True

    def __init__(self, screen) -> None:
        self.screen = screen
        self.run = True
        self.barrier_group = pygame.sprite.Group()
        self.tank_group = pygame.sprite.Group()
        self.health_group = []
        self.text = Text(screen)
        self.time_since_reset = -15000


    #creates initial barrier group to avoid a memory leak
    def create_map(self, world_data):
        for row in range(len(world_data)):
            for column in range(len(world_data[row])):
                if world_data[row][column] == 2:
                    self.player_x = column * 100
                    self.player_y = row * 100
                if world_data[row][column] == 1:
                    new_barrier = Barrier(column * 100, row * 100)
                    self.barrier_group.add(new_barrier)
                if world_data[row][column] == 3:
                    new_health = pygame.Rect(column * 100 + 37, row * 100 + 37, 25, 25)
                    self.health_group.append(new_health)

                if isinstance(world_data[row][column], list):
                    Game.enemy_count += 1
                    if world_data[row][column][0] == 1:
                        new_enemy = Enemy(column * 100 + 20, row * 100 + 20, world_data[row][column][1], world_data[row][column][2])
                        self.tank_group.add(new_enemy)
                    if world_data[row][column][0] == 2:
                        new_enemy = Trishot(column * 100 + 20, row * 100 + 20, world_data[row][column][1], world_data[row][column][2])
                        self.tank_group.add(new_enemy)
                    if world_data[row][column][0] == 3:
                        new_enemy = Seeker(column * 100 + 20, row * 100 + 20, world_data[row][column][1], world_data[row][column][2])
                        self.tank_group.add(new_enemy)

    #handles initial and all subsequent player spawns 
    def spawn_player(self):
        if Game.respawn == True and not Game.lives == 0:
            main_player = Tank(self.player_x, self.player_y)
            self.player = main_player
            self.tank_group.add(main_player)
            Game.respawn = False
            Tank.total_missel_group.empty()

    #handles key pushes
    def handle_events(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]:
            self.player.rotate_tank(3, self.barrier_group)
        if pressed[pygame.K_d]:
            self.player.rotate_tank(-3, self.barrier_group)
        if pressed[pygame.K_w]:
            self.player.move_tank(-3, self.barrier_group)
        if pressed[pygame.K_s]:
            self.player.move_tank(3, self.barrier_group)

    #handles single button presses
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    Game.quit_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.tank_shoot()

    #moves missles every game loop
        for missel in Tank.total_missel_group:
            missel.move_missel(self.barrier_group)

    #moves seeker missels
        for tank in self.tank_group:
            if isinstance(tank, Seeker):
                for seeker in tank.seeker_group:
                    seeker.move_missel(self.barrier_group)

        for health in self.health_group:
            if Game.lives < 3:  
                if health.colliderect(self.player.rect):
                    self.health_group.remove(health)
                    Game.lives += 1


    #checks for any tank collisions with missels
        for tank in self.tank_group:
            tank.tank_hit(self.player)


    #checks for each enemy to shoot
        for tank in self.tank_group:
            if not tank == self.player:
                tank.tank_shoot(self.player)

    #drawing function
    def draw_window(self, level):
        self.screen.fill((220, 220, 220))

        for health in self.health_group:
            pygame.draw.rect(self.screen, (255, 0, 0), health)

        #draws finish square for player after all enemies are dead
        if self.enemy_count == 0:
            finish = pygame.Rect(600, 100, 100 ,100)
            pygame.draw.rect(self.screen,(124,252,0), finish)
            self.text.draw_text("FINISH", (0,0,0), finish)
            if self.player.rect.colliderect(finish):
                Tank.total_missel_group.empty()
                self.run = False

        #draws barriers on screen
        for barrier in self.barrier_group: 
            self.screen.blit(barrier.image, (barrier.x, barrier.y))

        #draws tanks on screen
        for tank in self.tank_group: 
            self.screen.blit(tank.image, tank.rect)

        #draws Health UI
        health = pygame.Rect(0, 0, 200, 50)
        pygame.draw.rect(self.screen, (220, 220, 220), health)
        pygame.draw.rect(self.screen, (0, 0, 0), health, 2)
        self.text.draw_UI_text("LIVES",(0, 0, 0), health)
        for life in range(self.lives):
            life = pygame.Rect(health.width - 40 - (35 * life), health.center[1] - 25//2, 25, 25)
            pygame.draw.rect(self.screen, (255, 0, 0), life)

        #draws level name UI
        level_number = pygame.Rect(self.screen.get_width()//2 - 100, 0, 200, 60)
        pygame.draw.rect(self.screen, (220, 220, 220), level_number)
        pygame.draw.rect(self.screen, (0, 0, 0), level_number, 2)
        self.text.draw_text(f"LEVEL {level}", (0, 0, 0), level_number)

        #handles reset button
        reset = pygame.Rect(self.screen.get_width() - 150, 0, 150, 50)
        pygame.draw.rect(self.screen, (220, 220, 220), reset)
        if pygame.time.get_ticks() - self.time_since_reset <= 15000 and self.time_since_reset > 0:
            loading = pygame.Rect(self.screen.get_width() - 150, 0, (pygame.time.get_ticks() - self.time_since_reset)//100, 50)
            pygame.draw.rect(self.screen, (169, 169, 169), loading)
        pygame.draw.rect(self.screen, (0, 0, 0), reset, 2)
        self.text.draw_UI_text_centered("RESET", (0, 0, 0), reset)
        pos = pygame.mouse.get_pos()
        if reset.collidepoint(pos):
            if pygame.time.get_ticks() - self.time_since_reset >= 15000:
                if pygame.mouse.get_pressed()[0]:
                    self.time_since_reset = pygame.time.get_ticks()
                    self.player.source_rect.x = self.player_x
                    self.player.source_rect.y = self.player_y
                    self.player.rect.x = self.player_x
                    self.player.rect.y = self.player_y
                    self.player.rotate_tank(-self.player.rotation, self.barrier_group)

        # for tank in self.tank_group:
        #     if isinstance(tank, Enemy):
        #         pygame.draw.rect(self.screen, (0,0,0), tank.rect)
                  
        for projectile in Tank.total_missel_group:
            self.screen.blit(projectile.image, projectile.rect)

        # for tank in self.tank_group:
        #     if isinstance(tank, Seeker):
        #         for seeker in tank.seeker_group:
        #             self.screen.blit(seeker.image, seeker.rect)

        pygame.display.update()