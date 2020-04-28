import pygame
from pygame.locals import*
screen=pygame.display.set_mode((1250,720))
zigzags = pygame.image.load('zigzags.png')
pygame.init()
clock=pygame.time.Clock()
boxx=200
boxy=200
image = pygame.Surface([20,20]).convert_alpha()
image.fill((255,255,255))
speed = 5   # larger values will move objects faster

while True :
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
            quit()
    screen.blit(zigzags, (0, 0))
    zigzags.scroll(-5, 0)
    # I did modulus 720, the surface width, so it doesn't go off screen
    screen.blit(image,((boxx + speed) % 720, (boxy + speed) % 720))
    pygame.display.update()
    clock.tick(60)