import pygame
from sys import exit

# initialize the pygame library to exicute the pygames commands
pygame.init()

# title for the pygame window
pygame.display.set_caption("Runner")

# call the GUI
screen = pygame.display.set_mode((800, 400))

# inifinie loop for the continous game running
while True:
    # to close the game when the user wants to cloase it
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    # to put the drawn code on the display
    pygame.display.update()
