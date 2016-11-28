#for my project I am going to create astroid 
import pygame, sys, os, random, math
from pygame.locals import *

pygame.mixer.pre_init()
pygame.init()                      
fps = pygame.time.Clock()



SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
BG_COLOR = 150, 150, 80
CREEP_FILENAMES = [
    'bluecreep.png',
    'pinkcreep.png',
    'graycreep.png']
N_CREEPS = 20

pygame.init()
screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
clock = pygame.time.Clock()

# Create N_CREEPS random creeps.



creeps = []
for i in range(N_CREEPS):
    creeps.append(Creep(screen,
                        choice(CREEP_FILENAMES),
                        (   randint(0, SCREEN_WIDTH),
                            randint(0, SCREEN_HEIGHT)),
                        (   choice([-1, 1]),
                            choice([-1, 1])),
                        0.1))

class Creep(Sprite):
    """ A creep sprite that bounces off walls and changes its
        direction from time to time.
    """
    def __init__(
            self, screen, img_filename, init_position,
            init_direction, speed):
    creeps.append(Creep(screen,
                    choice(CREEP_FILENAMES),
                    (   randint(0, SCREEN_WIDTH),
                        randint(0, SCREEN_HEIGHT)),
                    (   choice([-1, 1]),
                        choice([-1, 1])),
                    0.1))

while True:

    time_passed = clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    
    screen.fill(BG_COLOR)

   
    for creep in creeps:
        creep.update(time_passed)
        creep.blitme()


def update(self, time_passed):
	self._change_direction(time_passed)
	self.image = pygame.transform.rotate(
    self.base_image, -self.direction.angle)

 	displacement = vec2d(self.direction.x * self.speed * time_passed, self.direction.y * self.speed * time_passed)
 	self.image_w, self.image_h = self.image.get_size()
bounds_rect = self.screen.get_rect().inflate(
                -self.image_w, -self.image_h)

	if self.pos.x < bounds_rect.left:
    	self.pos.x = bounds_rect.left
    	self.direction.x *= -1
	elif self.pos.x > bounds_rect.right:
   		self.pos.x = bounds_rect.right
    	self.direction.x *= -1
	elif self.pos.y < bounds_rect.top:
    	self.pos.y = bounds_rect.top
    	self.direction.y *= -1
	elif self.pos.y > bounds_rect.bottom:
    	self.pos.y = bounds_rect.bottom
    	self.direction.y *= -1

	self.pos += displacement

    pygame.display.flip()


