print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away.")
        
elif door == "2":
    print("You stare into the endless abyss of Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    print("4. Poke him in the eye.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
        
    elif insanity == "3":
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
    
    elif insanity == "4":
        print("'Ouch! What the hell? I was just meditating!' says Cthulhu, his eye watering in pain. He readies a gargantuan tentacle to punch you in the nose.")
        print("1. Run away.")
        print("2. Block.")
        
        punch = input("> ")
        
        if punch == "1":
            print("You skedaddle. Good job!")
        elif punch == "2":
            print("Cthulhu pulls his punch at the last moment. 'Just kidding' he chuckles. Good job!")
        else:
            print("He pulverises you into a thin paste. Good job!")
      
else:
    print("You stumble around and fall on a knife and die. Good job!")