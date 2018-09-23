class Character():
    '''Base class for Enemies, NPCs, random Animals, with name, 
    description, conversation and triggerword attributes
    '''
    def __init__(self, char_name, char_descr):
        #NB need positional defaults in init for conversation and triggerword?
        self.char_name = char_name
        self.char_descr = char_descr
        self.char_defaultresponse = None
        self.dialtriggers = {}
        
    def get_name(self):
        '''Getter for character name'''
        return self.char_name
        
    def get_char_descr(self):
        '''Getter for char description'''
        return self.char_descr
        
    def set_char_defaultresponse(self, char_defaultresponse):
        '''Setter for default character response'''
        self.char_defaultresponse = char_defaultresponse

    def fight(self):
        '''default is pacifism'''
        print(self.char_name, "is not interested in fighting you.")
        
    def set_response(self, dial_trigger, dial_response):
        '''Setter for character dialogue triggers ie specific responses'''
        self.triggers[dial_trigger] = dial_response
        
    def get_response(self, dial_trigger):
        '''Getter for dialogue - NB need to include charname in this return?'''
        Response = self.char_defaultresponse
        if self.dialtriggers:
            if dial_trigger in self.dialtriggers:
                response = self.dialtriggers[dial_trigger]
            
        return response
        
class Enemy(Character):
    
    def __init__(self, char_name, char_descr, enemy_hitpoints, enemy_speed, enemy_damage):
    
        super.__init__(self, char_name, char_descr):
        self.enemy_hitpoints = enemy_hitpoints
        self.enemy_speed = enemy_speed
        self.enemy_damage = enemy_damage
        self.enraged = False
        #Flag to use for later implementation of chasing mechanic
        self.alive = True
        
    def fight_round(self, player_speed, dice_roll, player_damage)
        '''Override default Character behaviour - fight a single round of combat.'''
        attack = player_speed + dice_roll
        if attack > self.enemy_speed:
            if self.enemy_hitpoints >  player_damage:
                self.enemy_hitpoints -= player_damage
                print("You surprise {} and deal {}pts of damage!".format(self.char_name, player_damage))
                self.enraged = True
                outcome = "WIN"
            else:
                print("You defeat {}!".format(self.char_name))
                self.alive = False
        elif attack == self.enemy_power:
            print("You dodge each other's attack!")
            self.enraged = True
            outcome = "DRAW"
        else:
            print("{} savagely counterattacks for {}pts of damage!".format(self.char_name, enemy_damage))
            outcome = "LOSE"
            
        return outcome
