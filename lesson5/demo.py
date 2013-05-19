import pygame
import random

pygame.init()
screen = pygame.display.set_mode((700,500))

background = pygame.image.load('background.jpg')
# sheet = pygame.image.load('sonic2.gif') #Load the sheet
# sheet = pygame.transform.scale(sheet, (1680 * SIZE_MULTI ,100 * SIZE_MULTI))

done = False

bird = pygame.image.load('bird.png')
bird1_x = -120
bird2_x = 280

b1 = pygame.image.load('building1.png')
b2 = pygame.transform.scale(pygame.image.load('building2.png'), (160,400))
b3 = pygame.image.load('building3.png')
b4 = pygame.image.load('building2.png')
b5 = pygame.transform.scale(pygame.image.load('building4.png'), (160,400))


cloud = pygame.image.load('cloud.png')
cloud_x = 0

while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    screen.blit(background, (0, 0))

    screen.blit(b1, (30, 300))
    screen.blit(b4, (400, 240))
    screen.blit(b3, (320, 340))
    
    screen.blit(cloud, (cloud_x, 350))
    
    screen.blit(b2, (90, 380))    
    screen.blit(b5, (380, 380))
        
    screen.blit(bird, (bird1_x, 20))
    screen.blit(bird, (bird2_x, 100))    
    
    bird1_x -= 5
    if bird1_x < -120: 
       bird1_x =  720
       
    bird2_x -= 8
    if bird2_x < -120: 
      bird2_x =  720
    
    cloud_x += 3
    if cloud_x > 710: 
      cloud_x =  -150
    
    pygame.display.update()
    # pygame.time.delay(latency)

