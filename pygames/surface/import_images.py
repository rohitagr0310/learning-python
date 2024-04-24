import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_screen = pygame.image.load("resources/Sky.png")
ground_screen = pygame.image.load("resources/ground.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_screen, (0, 0))
    screen.blit(ground_screen, (0, 300))

    pygame.display.update()
    clock.tick(60)
