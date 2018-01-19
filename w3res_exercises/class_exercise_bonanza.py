class NumToRomanConvertor():

    def num_to_roman_convert(self, num):
        res = 0
        D = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'M':1000}
        for char in num:
            res += D.get(char)
        return res