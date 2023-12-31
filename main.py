import pygame, sys
import json
from game import Game

pygame.init()

#screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toy Tanks")
FPS = 60

#import tank images
RED_TANK = pygame.image.load("Red_Tank_Sprite.png").convert_alpha()
BLUE_TANK = pygame.image.load("Blue_Tank_Sprite.png").convert_alpha()

TEXT_FONT = pygame.font.SysFont("Arial", 30)
TITLE_FONT = pygame.font.SysFont("Arial", 120)


def draw_text(text, font, text_col, button):
    text_img = font.render(text, True, text_col)
    SCREEN.blit(text_img, (button.center[0] - text_img.get_width()//2, button.center[1] - text_img.get_height()//2))

def main():
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
        draw_text("Toy Tanks", TITLE_FONT, (0,0,0), TITLE)
        draw_text("START", TEXT_FONT, (0,0,0), START_BUTTON)
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

            #loads world data
            level_file = open(f'level{level}_data.json', 'r')
            world_data = json.load(level_file)

            #Create main gamed
            game = Game(SCREEN)
            game.create_map(world_data, RED_TANK, BLUE_TANK)
            
            while game.run:
                clock.tick(FPS)

                if Game.quit_game == True:
                    pygame.quit()
                    sys.exit()

                game.draw_window()
                game.handle_events()

        #end screen
            if level == TOTAL_LEVELS:
                running = False
                end_screen = True
                while end_screen  == True:
                    pos = pygame.mouse.get_pos()
                    SCREEN.fill((220, 220, 220))
                    TITLE = pygame.Rect(SCREEN.get_width()//2 - 300, 100, 600, 200)
                    RESTART_BUTTON = pygame.Rect(SCREEN.get_width()//2 - 150, SCREEN.get_height()//2 - 50, 300, 100)
                    pygame.draw.rect(SCREEN, (114,114,114), START_BUTTON)
                    draw_text("Winner!", TITLE_FONT, (0,0,0), TITLE)
                    draw_text("RESTART", TEXT_FONT, (0,0,0), START_BUTTON)
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


main()