#asking for input for people, cars and trucks and storing them in approp named variables
people = int(input('How many peoples? '))
cars = int(input('How many cars? '))
trucks = int(input('How many truckses? '))

#beginning of if logic blocks. If more cars than people (and people not 0) we shd take cars else not, otherwise we can't decide
if cars > people > 0:
    print("We should take the cars.")
elif 0 < cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
    
#more trucks than cars though, means take trucks instead (bit clumsy - needs an interrupt). Fewer trucks than cars (should go before people?)
if trucks > cars > 0:
    print("That's too many trucks.")
elif 0 < trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")
    
#Further comparison - more people than trucks? Take the trucks. I guess because trucks can hold more people? Poor analogy.
if people > trucks > 0:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's just stay home.")