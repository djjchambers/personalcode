import urllib.request, pickle

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
data = pickle.loads(urllib.request.urlopen(url).read())
for line in data:
	print(''.join(elmt[0] * elmt[1] for elmt in line))