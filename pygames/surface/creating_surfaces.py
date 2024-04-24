import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_screen = pygame.Surface((100, 200))
test_screen.fill("Red")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_screen, (0, 0))
    screen.blit(test_screen, (200, 0))
    screen.blit(test_screen, (400, 0))
    screen.blit(test_screen, (600, 0))
    screen.blit(test_screen, (100, 200))
    screen.blit(test_screen, (300, 200))
    screen.blit(test_screen, (500, 200))
    screen.blit(test_screen, (700, 200))

    pygame.display.update()
    clock.tick(60)
