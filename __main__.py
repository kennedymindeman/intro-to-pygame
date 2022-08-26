import pygame
import sys

window_height, window_width = 800, 400

pygame.init()
screen = pygame.display.set_mode((window_height, window_width))
clock = pygame.time.Clock()
pygame.display.set_caption('Runner')

test_surface = pygame.Surface((window_height // 8, window_width // 2))
test_surface.fill('Red')

while True:
    # update loop
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(test_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)