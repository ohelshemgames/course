import pygame
import random

pygame.init()

SIZE = [700,500]

objects = []
NEW_BALL_EVENT = 30

# Set the height and width of the screen

background = pygame.image.load('background-forest.jpg')
ball = pygame.image.load('ball.png')
bar = pygame.image.load('bar.png')

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Ball Game")

screen.blit(background, (0, 0))

bar_x = 250
bar_y = 450
bar_speed = 0

ball_x = 50
ball_y = 50
ball_x_speed = 10
ball_y_speed = -10

done = False
latency = 50

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_LEFT:
                bar_speed = -10
            if event.key == pygame.K_RIGHT:
                bar_speed = 10
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                bar_speed = 0
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                bar_speed = 0

    bar_x = bar_x + bar_speed
    if bar_x < 0:
        bar_x = 0
    if bar_x + bar.get_width() >= SIZE[0]:
        bar_x = SIZE[0] - bar.get_width()

    old_ball_x = ball_x
    old_ball_y = ball_y

    ball_x = ball_x + ball_x_speed
    ball_y = ball_y + ball_y_speed

    if ball_x <= 0 or ball_x + ball.get_width() >= SIZE[0]:
        ball_x_speed = -ball_x_speed
    if ball_y <= 0 or ball_y + ball.get_height() >= SIZE[1]:
        ball_y_speed = -ball_y_speed

    if ball_y + ball.get_height() >= bar_y and old_ball_y + ball.get_height() < bar_y and bar_x <= ball_x + ball.get_width() and ball_x <= bar_x + bar.get_width():
        ball_y_speed = -ball_y_speed

    if ball_y + ball.get_height() >= SIZE[1]:
        done = True

    # Draw the ball in the new position
    screen.blit(background, (0, 0))
    screen.blit(bar, (bar_x, bar_y))
    screen.blit(ball, (ball_x, ball_y))
    
    pygame.display.update()

    pygame.time.delay(latency)

# Game Over

font = pygame.font.Font(None, 36)
text = font.render("Game Over", 1, (0, 0, 0), (255, 255, 255))
textpos = text.get_rect(centerx = SIZE[0] / 2, centery = SIZE[1] / 2)
screen.blit(text, textpos)
pygame.display.update()

done = False
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            done = True # Flag that we are done so we exit this loop
    pygame.time.delay(100)

pygame.quit()
