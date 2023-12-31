import pygame
from barrier import Barrier
from tank import Tank
from enemy import Enemy

class Game:
    quit_game = False
    #total count of enemies to determin when level finish should appear
    enemy_count= 0 
    def __init__(self, screen) -> None:
        self.screen = screen
        self.run = True
        self.barrier_group = pygame.sprite.Group()
        self.tank_group = pygame.sprite.Group()


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

    #checks for any tank collisions with missels
        for tank in self.tank_group:
            tank.tank_hit()

    #checks for each enemy to shoot
        for tank in self.tank_group:
            if isinstance(tank, Enemy):
                tank.tank_shoot(self.player)

    #creates initial barrier group to avoid a memory leak
    def create_map(self, world_data, red_tank, blue_tank):
        for row in range(len(world_data)):
            for column in range(len(world_data[row])):
                if world_data[row][column] == 2:
                    main_player = Tank(red_tank, column * 100, row * 100)
                    self.screen.blit(main_player.image, (column * 100, row * 100))
                    self.player = main_player
                    self.tank_group.add(main_player)
                if world_data[row][column] == 1:
                    new_barrier = Barrier(column * 100, row * 100)
                    self.screen.blit(new_barrier.image, (column * 100, row * 100))
                    self.barrier_group.add(new_barrier)
                if world_data[row][column] == 3:
                    new_enemy = Enemy(blue_tank, column * 100 + 20, row * 100 + 20)
                    self.screen.blit(new_enemy.image, (column * 100 + 20, row * 100 + 20))
                    self.tank_group.add(new_enemy)
                    Game.enemy_count += 1

    #drawing function
    def draw_window(self):
        self.screen.fill((220, 220, 220))

        #draws finish square for player after all enemies are dead
        if self.enemy_count == 0:
            finish = pygame.Rect(600, 100, 100 ,100)
            pygame.draw.rect(self.screen,(124,252,0), finish)
            if self.player.rect.colliderect(finish):
                # Tank.total_missel_group.empty()
                self.run = False

        #draws tanks on screen
        for tank in self.tank_group: 
            self.screen.blit(tank.image, tank.rect)
    
        #draws barriers on screen
        for barrier in self.barrier_group: 
            self.screen.blit(barrier.image, (barrier.x, barrier.y))

        # for tank in self.tank_group:
        #     if isinstance(tank, Enemy):
        #         pygame.draw.rect(self.screen, (0,0,0), tank.rect)
                  
        for projectile in Tank.total_missel_group:
            self.screen.blit(projectile.image, projectile.rect)
        pygame.display.update()