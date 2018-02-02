'''
Sample use of drawing commands

Sample Python/Pygame programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science
'''

# Import a library of functions called 'pygame'
import pygame

# Initialise the game engine
pygame.init()

# Define colors
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

pi = 3.141592653

#Set the height and width of screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Example code for the draw module')

# Loop until user clicks the X
done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    # All drawing code happens after the for loop but
    # Inside the main while done == False loop.
    
    # Clear screen and set BG
    screen.fill(white)
    
    # Draw green line from (0,0) to (50,75)
    # 5 px wide
    pygame.draw.line(screen, green, [0,0], [50,30], 5)
    
    # Draw black line over it
    pygame.draw.lines(screen, black, False, [[0,80], [50,90], [200,80], [220,30]], 5)
    
    # Draw another line
    pygame.draw.aaline(screen, green, [0,50], [50,80], True)
    
    # Draw rectangular outline
    pygame.draw.rect(screen, black, [75,10,50,20], 2)
    
    # Draw solid rect
    pygame.draw.rect(screen, black, [150,10,50,20])
    
    # Draw ellipse outline using rect as outside boundaries
    pygame.draw.ellipse(screen, red, [225,10,50,20], 2)
    
    # Draw solid ellipse using rect as boundaries
    pygame.draw.ellipse(screen, red, [300,10,50,20])
    
    # Draw triangle using polygon cmd
    pygame.draw.polygon(screen, black, [[100,100], [0,200], [200,200]], 5)
    
    # Draw arc as part of ellipse
    # Use radians to determine what angle to draw
    pygame.draw.arc(screen, black, [210,75,150,125], 0, pi / 2, 2)
    pygame.draw.arc(screen, green, [210,75,150,125], pi /2, pi, 2)
    pygame.draw.arc(screen, blue, [210,75,150,125], pi, 3 * pi)
    pygame.draw.arc(screen, red, [210,75,150,125], 3 * pi / 2, 2 * pi, 2)
    
    # Draw a circle
    pygame.draw.circle(screen, blue, [60,250], 40)
    
    # Update screen
    # This MUST happen after all other drawing cmds
    pygame.display.flip()
    
    # This limits the while loop to max 10ps
    # Leave it out and we'll use all the CPU we can
    clock.tick(60)
    
# Be IDLE friendly
pygame.quit()