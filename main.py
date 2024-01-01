import pygame, sys
import json
from game import Game
from text import Text

pygame.init()

#screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toy Tanks")
FPS = 60

#import tank images
RED_TANK = pygame.image.load("Red_Tank_Sprite.png").convert_alpha()
BLUE_TANK = pygame.image.load("Blue_Tank_Sprite.png").convert_alpha()

def main():
    text = Text(SCREEN)
    START_SCREEN = True
    TOTAL_LEVELS = 2

    #sets frame rate
    clock = pygame.time.Clock()
    clock.tick(FPS)

    #start screen
    while START_SCREEN:
        pos = pygame.mouse.get_pos()
        SCREEN.fill((220, 220, 220))
        TITLE = pygame.Rect(SCREEN.get_width()//2 - 300, 100, 600, 200)
        START_BUTTON = pygame.Rect(SCREEN.get_width()//2 - 150, SCREEN.get_height()//2 - 50, 300, 100)
        pygame.draw.rect(SCREEN, (114,114,114), START_BUTTON)
        text.draw_text_title("Toy Tanks", (0,0,0), TITLE)
        text.draw_text("START", (0,0,0), START_BUTTON)
        pygame.display.update()
        if START_BUTTON.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                START_SCREEN = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    #main level loop
    running = True
    while running == True:
        for level in range(1, TOTAL_LEVELS + 1):    
            Game.respawn = True

            #loads world data
            level_file = open(f'level{level}_data.json', 'r')
            world_data = json.load(level_file)

            #Create main gameda
            game = Game(SCREEN)
            game.create_map(world_data, BLUE_TANK)
            
            while game.run:
                clock.tick(FPS)

                if Game.quit_game == True:
                    pygame.quit()
                    sys.exit()

                game.spawn_player(RED_TANK)
                game.handle_events()
                game.draw_window()

            #death screen
                if Game.lives == 0:
                    running = False
                    death_screen = True
                    while death_screen  == True:
                        pos = pygame.mouse.get_pos()
                        SCREEN.fill((220, 220, 220))
                        TITLE = pygame.Rect(SCREEN.get_width()//2 - 300, 100, 600, 200)
                        RESTART_BUTTON = pygame.Rect(SCREEN.get_width()//2 - 150, SCREEN.get_height()//2 + 100, 300, 100)
                        pygame.draw.rect(SCREEN, (114,114,114), RESTART_BUTTON)
                        text.draw_text_title("DEAD", (0,0,0), TITLE)
                        text.draw_text("RESTART", (0,0,0), RESTART_BUTTON)
                        pygame.display.update()
                        if RESTART_BUTTON.collidepoint(pos):
                            if pygame.mouse.get_pressed()[0]:
                                Game.lives = 3
                                death_screen = False
                                Game.enemy_count = 0
                                return "Done"
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

        #end screen
            if level == TOTAL_LEVELS:
                running = False
                end_screen = True
                while end_screen  == True:
                    pos = pygame.mouse.get_pos()
                    SCREEN.fill((220, 220, 220))
                    TITLE = pygame.Rect(SCREEN.get_width()//2 - 300, 100, 600, 200)
                    RESTART_BUTTON = pygame.Rect(SCREEN.get_width()//2 - 150, SCREEN.get_height()//2 - 50, 300, 100)
                    pygame.draw.rect(SCREEN, (114,114,114), RESTART_BUTTON)
                    text.draw_text_title("WINNER!", (0,0,0), TITLE)
                    text.draw_text("RESTART", (0,0,0), RESTART_BUTTON)
                    pygame.display.update()
                    if RESTART_BUTTON.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0]:
                            end_screen = False
                            running = True
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()


    pygame.quit()
    sys.exit()

def run_game():
    while True:
        main()

run_game()