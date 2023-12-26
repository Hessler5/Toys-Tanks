import pygame
from tank import Tank
from game import Game

pygame.init()

#screen setup
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toy Tanks")
FPS = 60

#import main player sprite
RED_TANK = pygame.image.load("Red_Tank_Sprite.png")
PLAYER = Tank(RED_TANK, 50, 50)

#Create main game
game = Game(SCREEN, PLAYER)

def main():
    clock = pygame.time.Clock()

    while game.run:
        clock.tick(FPS)

        game.draw_window(PLAYER)
        game.handle_events()
 
        


    pygame.quit()


main()