intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"

trantab = str.maketrans(intab, outtab)

str = "http://www.pythonchallenge.com/pc/def/map.html"
print(str.translate(trantab))
