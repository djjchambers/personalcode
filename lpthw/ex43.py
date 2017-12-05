from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):
    
    def enter(self):
        print("Nothing to see here yet!")
        print("Create some subclasses and implement enter to override this text.")
        # if nothing is defined for the Scene, it'll enter this function and exit with an error
        exit[1]

        
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene.map
    
    def play(self):
        pass