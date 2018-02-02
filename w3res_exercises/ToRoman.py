class Roman():
    ronumers = {'M': 1000, 'CM':900, 'D': 500, 'CD':400, 'C': 100, 'DC':90, 'L': 50, 'XL':40, 'X': 10, 'IX':9, 'V': 5, 'IV':4, 'I': 1}
    rnumorder = ronumers.keys()

class ToRoman(Roman):
    def __init__(self, num):
        self.num = num
        
    def num_to_rom(self):
        '''
        Floor div by each numeral pair adding to a string,
        num becomes the remainder each iteration.
        '''
        res = ''
        for rnum in Roman.rnumorder:
            res += (self.num // (Roman.ronumers.get(rnum)) * rnum)
            self.num = (self.num % (Roman.ronumers.get(rnum)))
        return res
        

class FromRoman(Roman):
    def __init__(self, rom):
        self.rom = rom
    
    def rom_to_num(self):
        '''
        Search for each numeral in rom,
        accumulating result
        '''
        res = 0
        i = 0
        while len(self.rom) > 0:
            for rnum in Roman.rnumorder:
                size = len(rnum)
                print(size)
                if self.rom[0:size] == rnum:
                    print('Found:', rnum)
                    res += Roman.ronumers.get(rnum)
                    print(res)
                    self.rom = self.rom[size:]
                else:
                    print('Not Found:', rnum)
            i += 1
        return res
    
to_roman_01 = ToRoman(2134)
temp = (to_roman_01.num_to_rom())

from_roman_01 = FromRoman(temp)
print(from_roman_01.rom_to_num())