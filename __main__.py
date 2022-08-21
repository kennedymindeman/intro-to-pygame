from turtle import window_width
import pygame

window_height, window_width = 800, 600

pygame.init()
screen = pygame.display.set_mode((window_height, window_width))

while True:
    # update loop
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()