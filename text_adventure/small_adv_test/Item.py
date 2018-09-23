class Item():
    '''Item class with name, description, value, weight attributes
    plus flags for containing and destructibility
    '''
    def __init__(self, item_name, item_descr, value, weight):
        self.item_name = item_name
        self.item_descr = item_descr
        self.value = value
        self.weight = weight
        self.iscontainer = False
        self.destructible = False
        
    def get_name(self):
        '''Getter for item name'''
        return self.item_name
    
    def set_descr(self, item_descr):
        '''Setter for item description'''
        self.item_descr = item_descr
        
    def get_descr(self):
        '''Getter for item description'''
        return self.item_descr
        
    def get_weight(self):
        '''Getter for weight attr'''
        return self.weight
        
    def set_weight(self, weight):
        '''Setter for weight in case of status change'''
        self.weight = weight