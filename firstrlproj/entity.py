import tcod as libtcod
import math

from render_functions import RenderOrder


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, name, blocks=False, render_order=RenderOrder.CORPSE, fighter=None, ai=None, item=None, inventory=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.render_order = render_order
        self.fighter = fighter
        self.ai = ai
        self.item = item
        self.inventory = inventory
        
        if self.fighter:
            self.fighter.owner = self
            
        if self.ai:
            self.ai.owner = self
            
        if self.item:
            self.item.owner = self
            
        if self.inventory:
            self.inventory.owner = self
        
    def move(self, dx, dy):
        # move the entity by a given amount
        self.x += dx
        self.y += dy
        
    def move_towards(self, target_x, target_y, game_map, entities):
        dx = target_x - self.x
        dy = target_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        
        if not (game_map.is_blocked(self.x + dx, self.y + dy) or get_blocking_entities_at_location(entities, self.x + dx, self.y + dy)):
            self.move(dx, dy)
            
    def move_astar(self, target, entities, game_map):
        # Create a FOV map that has the dimensions of the map
        fov = libtcod.map_new(game_map.width, game_map.height)
        
        # Scan the current map each turn and set all walls as unwalkable
        for y1 in range(game_map.height):
            for x1 in range(game_map.width):
                libtcod.map_set_properties(fov, x1, y1, not game_map.tiles[x1][y1].block_sight, not game_map.tiles[x1][y1].blocked)
                
        # Scan all objects to see if there are objects that must be navigated around
        # Check also that object itself isn't self or target (so start and end points are free)
        # AI class handles situation if self is next to target so it will not use thia A* function anyway
        for entity in entities:
            if entity.blocks and entity != self and entity !=target:
                # Set the tile as wall so must be nav'd around
                libtcod.map_set_properties(fov, entity.x, entity.y, True, False)
                
        # Allocate a A* path
        # The 1.41  is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohib'd
        my_path = libtcod.path_new_using_map(fov, 1.41)
        
        # Compute the path between self and target's coords
        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)
        
        # Check if path exists, and in this case if < 25 tiles
        # Path size matters if you want the monster to use alternative longer paths (eg through other rooms) if eg the player is in a corridor
        # Makes sense to keep path size low to keep monsters from taking far away alternative
        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            # Find next coords in computed full path
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                # Set self's coords to next path tile
                self.x = x
                self.y = y
                
        else:
            # Keep old move function as backup for when no paths exist (eg player blocks corridor)
            self.move_towards(target.x, target.y, game_map, entities)
            
            # Delete path to free mem
        libtcod.path_delete(my_path)
    def distance_to(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
        
def get_blocking_entities_at_location(entities, destination_x, destination_y):
    for entity in entities:
        if entity.blocks and entity.x == destination_x and entity.y == destination_y:
            return entity