import pygame, sys, json
from game import Game
from text import Text
from scenes import Scenes

pygame.init()

#screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toy Tanks")
FPS = 60
TOTAL_LEVELS = 5
text = Text(SCREEN)

def main():

    #sets frame rate
    clock = pygame.time.Clock()
    clock.tick(FPS)
    scenes = Scenes(SCREEN)

    #start screen
    scenes.start_screen()

    #main level loop
    while True:
        for level in range(1, TOTAL_LEVELS + 1):    
            Game.respawn = True

            #loads world data
            level_file = open(f'levels/level{level}_data.json', 'r')
            world_data = json.load(level_file)

            #Create main gameda
            game = Game(SCREEN)
            game.create_map(world_data)
            
            while game.run:
                clock.tick(FPS)

                if Game.quit_game == True:
                    pygame.quit()
                    sys.exit()

                game.spawn_player()
                game.handle_events()
                game.draw_window(level)

            #death screen
                if scenes.reset_screen() == True:
                    return "Done"

        #end screen
            scenes.end_screen(level, TOTAL_LEVELS)

#main function placed in a loop to facilitate restarting 
def run_game():
    while True:
        main()

run_game()