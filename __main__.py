import pygame
import sys

window_height, window_width = 800, 600

pygame.init()
screen = pygame.display.set_mode((window_height, window_width))
clock = pygame.time.Clock()
pygame.display.set_caption('Runner')

while True:
    # update loop
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)