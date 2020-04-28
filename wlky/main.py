import pygame
import os

screen=pygame.display.set_mode((1250,720))
pygame.init()
clock=pygame.time.Clock()
image =

while True :
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
            quit()
    image.scroll(10,10)
    # I did modulus 720, the surface width, so it doesn't go off screen
    screen.blit(image,((boxx + speed) % 720, (boxy + speed) % 720))
    pygame.display.update()
    clock.tick(60)

# class hill(object):
#    def __init__(self, height, width, stepth, xpos, ypos, distance, colour):
#        self.height = height
#        self.width = width
#        self.stepth = stepth
#        self.xpos = xpos
#        self.ypos = ypos
#        self.distance = distance
#        self.colour = colour




