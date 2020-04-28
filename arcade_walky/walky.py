# basic Arcade program using objects
# Displays a white window with a blue circle in middle

# Imports
import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Space Shooter"
SCALING = 2.0

# Classes
class Welcome(arcade.Window):
    '''Main welcome Window
    '''
    def __init__(self):
        '''Initialise the window
        '''
        
        # Call the parent class constructor
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
        # Set the bg window
        arcade.set_background_color(arcade.color.WHITE)
        
    def on_draw(self):
        '''Called whenever you need to draw your window
        '''
        
        # Clear screen and draw
        arcade.start_render()
        
        # Draw a blue circle
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
        )
        
class SpaceShooter(arcade.Window):
    '''Space Shooter side scroller game
    Pl starts on left, enemies appear right
    Pl can move anywhere, except offscreen
    Enemies fly to left at variable speed
    Collisions end game
    '''
    
    def __init__(self, width, height, title):
        '''Initialise game
        '''
        super().__init__(width, height, title)
        
        # Set up empty sprite lists
        self.enemies_list = arcade.SpriteList()
        self.clouds_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        
    def setup(self):
        ''' Get game ready to play
        '''
        
        # Set bg color
        arcade.set_background_color(arcade.color.SKY_BLUE)
        
        # Set up player
        self.player = arcade.Sprite("images/jet.png", SCALING)
        self.player.center_Y = self.height / 2
        self.player.left = 10
        self.all_sprites.append(self.player)
        
# Main code entry point
if __name__ == "__main__":
    app = Welcome()
    arcade.run()