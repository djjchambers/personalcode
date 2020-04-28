import pygame
import pygame.gfxdraw

from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((640,360))
background_image = pygame.image.load("zigzags.png").convert()

white = (255, 255, 255)
bottom = 200
top = 50
left = 200
right = 225
modifier = 20

window.blit(background_image, (0, 0))
pygame.gfxdraw.filled_polygon(window, [(bottom, left), (top, right), (top+modifier, left), (bottom, right)], (white))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    background_image.scroll(5, 0)
    pygame.display.flip()
    
#trapezoid works with modifier, but appears rotated to the left. Check coords
#next step is to scroll the rectangles and add more. 
# Added a bg image (diagonal stripes) in scrolltest_01.py and got it to scroll offscreen to the left with the pygame scroll() method. Leaves a jagged trail (guessing because we aren't updating the screen).
# Don't know what the difference is between blitting and updating.
# It's diaplaying the placeholders but static, not scrolling. I need to refer to pygame documentation for help with methods. Also drawing to screen.