'''
Pygame base template for opening a window

Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
'''

# imports go here
import pygame
import random

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BALL_SIZE = 25

# Set width and height of screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Ball:
    '''
    class to keep track of ball's location and vector.
    '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        
def make_ball():
    '''
    function to make new, random ball
    '''
    ball = Ball()
    # Starting pos of ball.
    # Take into account ball size so it isn't clipped
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
    
    # Speed & Direction of rect
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
    
    return ball

def main():
    '''
    Our main game program
    '''

    pygame.init()
    
    #Set height and width of game screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption('Bouncy')

    # Loop until user clicks close button
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    ball_list = []
    
    ball = make_ball()
    ball_list.append(ball)

    # Main Program Loop
    while not done:
        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn new ball.
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)
    
        # Game Logic goes here
        for ball in ball_list:
            #Move ball center
            ball.x += ball.change_x
            ball.y += ball.change_y
            
            # Bounce if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1
        # Screen clearing code goes here
    
        # Clear screen to white. No other drawing commands go above this.
        screen.fill(BLACK)
        # For BG img, replace this clear with blit bg
        
        # Drawing code goes here
        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)
            
        # Update screen with drawing.
        # This MUST happen after all the other drawing commands
        # draw...
        
        # Wrap up
        # Limit to 60fps
        clock.tick()

        pygame.display.flip()
    
    # Close window & quit
    pygame.quit
    
if __name__ = '__main__':
    main()