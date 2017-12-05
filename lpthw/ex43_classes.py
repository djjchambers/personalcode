class Scene(object):
    
    def enter(self):
        pass

    
class Engine(object):

    def __init__(self, scene_map):
        pass
    
    def play(self):
        # get input
        pass
    
class Death(Scene):
    
    def enter(self):
        print("You died.")
        pass
    
class CentralCorridor(Scene):
    
    def enter(self):
        print("You are in the Central Corridor.")
        pass
    
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print("You are in the Laser Weapon Armory.")
        pass
    
class TheBridge(Scene):
    
    def enter(self):
        print("You are on The Bridge.")
        pass
    
class EscapePod(Scene):
    
    def enter(self):
        print("You are in the Escape Pod.")
        pass
    

class Map(object):
    
    def __init__(self, start_scene):
        pass
        
    def north_exit(self, scene_name):
        pass
    
    def south_exit(self, scene_name):
        pass
    
    def east_exit(self, scene_name):
        pass
    
    def west_name(self, scene_name):
        pass
    
    def opening_scene(self):
        pass
    

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()