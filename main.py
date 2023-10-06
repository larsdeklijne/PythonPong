import pygame
import sys

# basis setup
pygame.init()
clock = pygame.time.Clock()

#dit is de main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Eerste PyGame: Pong')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #window update
    pygame.display.flip()
    clock.tick(60)