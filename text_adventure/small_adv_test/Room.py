class Room():

    def __init__(self, room_name, room_fulldescr, room_descr):
        '''Room initialiser with name, full description if first time visiting, normal description'''
        self.room_name = room_name
        self.room_fulldescr = room_fulldescr
        self.room_descr = room_descr
        self.visited = False
        self.exits = {}
        
    def get_name(self):
        '''Getter for room name
        NB is this print or return? We'll see!'''
        return self.name
        
    def describe(self):
        '''Getter for normal descr'''
        return self.room_descr
        
    def set_descr(self, room_descr):
        '''Setter for room_description in case of status change'''
        self.room_descr = room_descr

    def describe_verbose(self)
        '''Getter for verbose (ie first time) description'''
        return self.room_fulldescr
    
    def entered_room(self):
        '''Querying visited flag, to decide normal or verbose description'''
        if self.visited == False:
            self.visited = True
            return False
            
    def add_exit(self, direction, destination)
        '''Add exit to a Room's 'exits' dictionary'''
        self.exits[direction] = destination