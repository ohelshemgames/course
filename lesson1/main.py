import pygame
import random

pygame.init()

SIZE = [700,500]

# Set the height and width of the screen

background = pygame.image.load('background.jpg')

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Ball Game")

screen.blit(background, (0, 0))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

	# Update the screen with our changed
    pygame.display.update()

	# How much time between every loop
    pygame.time.delay(50)

# Game Over

pygame.display.update()

pygame.quit()
