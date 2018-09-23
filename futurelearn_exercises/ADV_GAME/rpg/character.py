class Character():

    def __init__(self, char_name, char_description):
        ''' Initialises a character instance with attributes name, description, conversation and money'''
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.money = 0
        self.location = None

    def describe(self):
        '''print out character description'''
        print( self.name + " is here!" )
        print( self.description )

    def set_conversation(self, conversation):
        '''Set what this character will say when talked to'''
        self.conversation = conversation
    
    def set_money(self, money):
        '''set amount of money'''
        self.money = money

    def talk(self):
        '''returns conversation if set, otherwise refusal message'''
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        '''Default for this class is no fighting'''
        print(self.name + " doesn't want to fight with you")
        return True
        
class Enemy(Character):
    '''initialises the Enemy class attribute weakness'''
    def __init__(self, char_name, char_description):

        super().__init__(char_name, char_description)
        self.weakness = None
        
    def fight(self, combat_item):
        '''fight with enemy - if using correct combat_item victory else defeat. Returns bool.
        NB functionality is split between this and the main game loop. Prob good idea to refactor
        '''
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + "crushes you, puny adventurer!")
            return False

    def set_weakness(self, item_weakness):
        '''set character's weakness (name of item)'''
        self.weakness = item_weakness
        
    def get_weakness(self):
        '''returns name of item character is vulnerable to'''
        return self.weakness
        
    def steal(self):
        '''This is implemented in the main game loop. Candidate for moving into this class?'''
        print("You steal from " + self.name)
        
class Friend(Character):
    '''initialises Friend class, inheriting from Character, with name and description'''
    def __init__(self, char_name, char_description):
    
        super().__init__(char_name, char_description)
        self.feeling = None
        
    def hug(self):
        '''not implemented'''
        print(self.name + " hugs you back!")