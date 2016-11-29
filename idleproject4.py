import pygame
from pygame.locals import *
 
# 2 - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))
 
# 3 - Load images
player = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.png")
grass = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.png")
castle = pygame.image.load("/Users/jessicastuart/Desktop/206project4/images/smiley.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    for x in range(int(width/grass.get_width()+1)):
        for y in range(int(height/grass.get_height()+1)):
            screen.blit(grass,(x*100,y*100))
        
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345 ))
    screen.blit(player, (100,100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0)
