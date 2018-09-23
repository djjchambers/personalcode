import itertools
import simplejson

firstname = ['Charlie', 'Theo', 'Rafe', 'Kit', 'Ziggy', 'Ivor', 'Albie', 'Bobby', 'Miles', 'Finn', 'Francis', 'Barnaby', 'Leo', 'Lewis', 'Felix']
secondname = ['Felix', 'Francis', 'Ivor', 'Barnaby', 'Leo']

results = {}
final = []

for name in itertools.product(firstname, secondname):
    if name[0] != name[1]:
        currname = (name[0], name[1], 'Chambers')
        print(' '.join(currname))
        response = input('Any good? 1.NO 2.OK 3.LIKE>')
        if int(response) > 1:
            results[currname] = int(response)
            
f = open('names.txt', 'w')
g = open('runnersup.txt', 'w')
for result in results:
    if results[result] == 3:
        simplejson.dump(' '.join(result), f)
    elif results[result] == 2:
        simplejson.dump(' '.join(result), g)
f.close()
g.close()