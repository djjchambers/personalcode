class Room():
    '''intialises Room class with name, description, linked_rooms and character attributes'''
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        
    def set_item(self, new_item):
        '''sets item to be within room'''
        self.item = new_item
        
    def get_item(self):
        '''returns item.name'''
        return self.item
        
    def set_character(self, new_character):
        '''sets character to be within room'''
        self.character = new_character
        
    def get_character(self):
        '''character getter - what character is in this room?
        NB only space for one character in room. Needs extending'''
        return self.character
        
    def set_description(self, room_description):
        '''room description setter'''
        self.description = room_description
        
    def get_description(self):
        '''room description getter'''
        return room_description
        
    def get_name(self):
        '''room name getter'''
        return self.name
        
    def set_name(self, room_name):
        '''room name setter'''
        self.name = room_name
        
    def describe(self):
        '''returns room description'''
        print(self.description)
        
    def link_room(self, room_to_link, direction):
        '''single use setter to link room to another one according to dict key'''
        self.linked_rooms[direction] = room_to_link
        #print( self.name + " linked rooms: " + repr(self.linked_rooms))
        
    def get_details(self):
        '''prints out room details including description and exits that are in dict'''
        print(self.name)
        print('-' * 11)
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print( 'The ' + room.get_name() + ' is ' + direction)
            
    def move(self, direction):
        '''if movement is in the mov dict, return the value of its key for use in the caller'''
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self