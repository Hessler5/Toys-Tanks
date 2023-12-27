import pygame
import json
from tank import Tank
from game import Game

pygame.init()

#screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toy Tanks")
FPS = 60

#import main player sprite
RED_TANK = pygame.image.load("Red_Tank_Sprite.png").convert_alpha()
PLAYER = Tank(RED_TANK, 50, 50)


#Create main game
game = Game(SCREEN, PLAYER)

#loads world data
level_file = open('level1_data.json', 'r')
world_data = json.load(level_file)

def main():
    clock = pygame.time.Clock()
    game.createBarriers(world_data)

    while game.run:
        clock.tick(FPS)

        game.draw_window(PLAYER)
        game.handle_events()
 
        


    pygame.quit()


main()