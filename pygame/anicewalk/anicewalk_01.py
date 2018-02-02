'''
Pygame base template for opening a window

Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
'''

# imports go here
import os, sys, math, pygame, pygame.mixer
from pygame.locals import *

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

# Set width and height of screen [width, height]
screen_size = SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500

class MyCircle():
    def __init__(self, (x, y), size, color=(255,255,255), width=1):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width
        
    def display(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size, self.width)

# Set display & get surf object
screen = pygame.display.set_mode(screen_size)
# Getting Clock object
clock = pygame.time.Clock()
# Set screen caption
pygame.display.set_caption('First Class!')

my_circle = MyCircle((100,100), 10, red)

# define vars for fps & continued running

fps_limit = 60
run_me = True
while run_me:
    # Limit the framerate
    clock.tick(fps_limit)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
            
    # Clear screen
    screen.fill(white)
    
    my_circle.display()
        
    # Display everything on screen
    pygame.display.flip()
    
# Quit game
pygame.quit()
sys.exit()