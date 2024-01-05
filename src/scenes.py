import pygame, sys
from text import Text
from game import Game
from tank import Tank
from enemy import Enemy

class Scenes():
    normal_mode = True
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.back_ground_color = (220, 220, 220)
        self.text = Text(screen)

    #utility quits pygame function
    def quit_pygame(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def start_screen(self):
        START_SCREEN_TANK = Tank(self.screen_width//2, self.screen_height//2 + 100)
        print(START_SCREEN_TANK.rect.center)
        START_SCREEN_TANK.rotate_tank(-90)
        TIME_SINCE_LAST_MOVE = 0
        while True:
            pos = pygame.mouse.get_pos()
            self.screen.fill((self.back_ground_color))
            self.screen.blit(START_SCREEN_TANK.image, START_SCREEN_TANK.rect)
            if pygame.time.get_ticks() - TIME_SINCE_LAST_MOVE > 4:
                TIME_SINCE_LAST_MOVE = pygame.time.get_ticks()
                if START_SCREEN_TANK.rect.center[0] < 1000 and START_SCREEN_TANK.rect.center[1] > 500 and START_SCREEN_TANK.rotation == -90:
                    START_SCREEN_TANK.move_tank(-1, [])
                elif START_SCREEN_TANK.rect.center[0] == 1000 and -90 <= START_SCREEN_TANK.rotation < 0:
                    START_SCREEN_TANK.rotate_tank(1)
                elif 535 > START_SCREEN_TANK.rect.center[1] > 100:
                    START_SCREEN_TANK.move_tank(-1, [])
                elif START_SCREEN_TANK.rect.center[1] == 100 and 0 <= START_SCREEN_TANK.rotation < 90:
                    START_SCREEN_TANK.rotate_tank(1)
                elif START_SCREEN_TANK.rect.center[0] > 200:
                    START_SCREEN_TANK.move_tank(-1, [])
                elif START_SCREEN_TANK.rect.center[0] == 200 and 90 <= START_SCREEN_TANK.rotation < 180:
                    START_SCREEN_TANK.rotate_tank(1)
                elif START_SCREEN_TANK.rect.center[1] < 535:
                    START_SCREEN_TANK.move_tank(-1, [])
                elif START_SCREEN_TANK.rect.center[0] == 200 and 180 <= START_SCREEN_TANK.rotation < 270:
                    START_SCREEN_TANK.rotate_tank(1) 
                elif START_SCREEN_TANK.rotation == 270:
                    START_SCREEN_TANK.rotation = -90
            TITLE = pygame.Rect(self.screen_width//2 - 300, 100, 600, 200)
            START_BUTTON = pygame.Rect(self.screen_width//2 - 150, self.screen_height//2 - 50, 300, 100)
            pygame.draw.rect(self.screen, (114,114,114), START_BUTTON)
            self.text.draw_text_title("Toy Tanks", (0,0,0), TITLE)
            self.text.draw_text("START", (0,0,0), START_BUTTON)
            MODE = pygame.Rect(self.screen_width - 250, self.screen_height - 225, 200, 50)
            self.text.draw_UI_text_centered("MODE SELECTION", (0,0,0), MODE)
            NORMAL_MODE = pygame.Rect(self.screen_width - 250, self.screen_height - 175, 200, 50)
            pygame.draw.rect(self.screen, (114,114,114), NORMAL_MODE)
            self.text.draw_UI_text_centered("NORMAL", (0,0,0), NORMAL_MODE)
            INVINCIBLE_MODE = pygame.Rect(self.screen_width - 250, self.screen_height - 100, 200, 50)
            pygame.draw.rect(self.screen, (114,114,114), INVINCIBLE_MODE)
            self.text.draw_UI_text_centered("INVINCIBILTY", (0,0,0), INVINCIBLE_MODE)
            if Scenes.normal_mode:
                pygame.draw.rect(self.screen, (0,0,0), NORMAL_MODE, 2)
            else:
                pygame.draw.rect(self.screen, (0,0,0), INVINCIBLE_MODE, 2)
            pygame.display.update()
            if START_BUTTON.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    break
            if INVINCIBLE_MODE.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    Scenes.normal_mode = False
            if NORMAL_MODE.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    Scenes.normal_mode = True
            self.quit_pygame()

    def reset_screen(self):
        if Game.lives == 0:
                    while True:
                        pos = pygame.mouse.get_pos()
                        self.screen.fill((self.back_ground_color))
                        TITLE = pygame.Rect(self.screen_width//2 - 300, 100, 600, 200)
                        RESTART_BUTTON = pygame.Rect(self.screen_width//2 - 150, self.screen_height//2 + 100, 300, 100)
                        pygame.draw.rect(self.screen, (114,114,114), RESTART_BUTTON)
                        self.text.draw_text_title("DEAD", (0,0,0), TITLE)
                        self.text.draw_text("RESTART", (0,0,0), RESTART_BUTTON)
                        pygame.display.update()
                        if RESTART_BUTTON.collidepoint(pos):
                            if pygame.mouse.get_pressed()[0]:
                                Game.lives = 3
                                Game.enemy_count = 0
                                Tank.total_missel_group.empty()
                                return True
                        self.quit_pygame()

    def end_screen(self, level, total_levels):
        if level == total_levels:
            while True:
                pos = pygame.mouse.get_pos()
                self.screen.fill((self.back_ground_color))
                TITLE = pygame.Rect(self.screen_width//2 - 300, 100, 600, 200)
                RESTART_BUTTON = pygame.Rect(self.screen_width//2 - 150, self.screen_height//2 + 100, 300, 100)
                pygame.draw.rect(self.screen, (114,114,114), RESTART_BUTTON)
                self.text.draw_text_title("WINNER!", (0,0,0), TITLE)
                self.text.draw_text("RESTART", (0,0,0), RESTART_BUTTON)
                pygame.display.update()
                if RESTART_BUTTON.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0]:
                        Game.lives = 3
                        Tank.total_missel_group.empty()
                        return "Done"
                self.quit_pygame()