class Item():
    '''initialises Item class with item_name attribute'''
    def __init__(self, item_name):
        self.name = item_name
        
    def get_name(self):
        '''returns name'''
        return self.name
        
    def set_name(self, item_name):
        '''name setter'''
        self.name = item_name
        
    def get_description(self):
        '''description getter'''
        return self.description
        
    def set_description(self, item_description):
        '''description setter'''
        self.description = item_description
        
    def describe(self):
        '''prints out description'''
        print(self.description)