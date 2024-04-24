import pygame
from sys import exit

pygame.init()
pygame.display.set_caption("Runner")

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()  # set the clock module to clock variable

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)  # setting the fps for the game
