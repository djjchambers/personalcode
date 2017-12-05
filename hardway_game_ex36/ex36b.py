from sys import exit

def room_start():
    global door_open
    door_open = False
    
    print("You are in the mucky cockpit of an old starship.")
    print("The windshield to the north shows many stars and many smudges.")
    
    if door_open == False:
        print("A metal door to the South is closed.")
    elif door_open == True:
        print("A metal door to the South is open.")
    print("On the ancient T1000 console are the words \'INTRUDER ALERT\'.")
    print("A crude diagram of the ship shows a flashing red dot two rooms to the South, in the airlock.")
    print("What do you want to do?")
    
    while True:
        choice = input('> ')
        
        if "south" in choice and door_open == False:
            print("The door is closed.")
        elif "south" in choice and door_open == True:
            print("The heavy metal door swings shut behind you.")
            room_engineering()
        elif "open" in choice and door_open == True:
            print("The door is already open!")
        elif "open" in choice and door_open == False:
            door_open = True   
            print("You heave the metal door open.")
        else:
            print("I don't understand.")
        
def room_engineering():
    global hatch_open
    global wrench_holding
    hatch_open = False
    wrench_holding = False
    door_open = True
    print("You are in a grimy engineering room. Metal benches line the walls.")
    print("You can see a wrench.")
    print("A metal door leads north and a hatch leads south.")
    
    while True:
        choice = input('> ')
        
        print(wrench_holding)
        
        if "north" in choice and door_open == True:
            print("The heavy metal door swings shut behind you.")
            room_start()
            print(wrench_holding)
        elif "close" in choice and "door" in choice:
            print("You close the door")
            door_open = False
            print(wrench_holding)
        elif "south" in choice and hatch_open == False:
            print("The hatch is closed!")
            print(wrench_holding)
        elif "south" in choice and hatch_open == True:
            print("You squeeze through the hatch.")
            room_airlock()
        elif "wrench" in choice:
            wrench_holding = True
            print("You pick up the heavy wrench.")
            print(wrench_holding)
        elif "hatch" in choice and wrench_holding == True:
            print("You wrench the lever open - the hatch swings free.")
            print(wrench_holding)
        elif "hatch" in choice and wrench_holding == False:
            print("You're not strong enough to do that by hand.")
            hatch_open = True
            print(wrench_holding)
        else:
            print("I don't understand.")
        
def room_airlock():
    print("You are in the airlock of an old starship.")
    print("The void of space yawns endlessly outside the glass airlock door.")
    print("There is a crack in the glass door.")
    print("An escape capsule door is open to the west.")
    print("A slavering alien monster confronts you.")
    print("What are you going to do?")
    
    while True:
        choice = input("> ")
        
        if "kill" or "alien" in choice:
            dead("The alien is too fast & powerful for you, it folds you into a little cube.")
        elif "throw" or "crack" or "smash" or "glass" in choice and not alien_dead:
            print("You heave the wrench at the glass, which explodes outwards.")
            print("The alien is sucked out into the gulf of space.")
            room_airlock_vacuum()
        elif "capsule" or "escape" in choice:
            dead("The alien is too fast. As you lunge for the door it grabs you and turns you into confetti.")
        else:
            print("No idea what that means.")
            
def room_airlock_vacuum():
    print("The ship's precious air is escaping through the smashed door.")
    print("There isn't much time!")
    print("What are you going to do?")
    while True:
        choice = input("> ")
        
        if "escape" or "capsule" in choice:
            print("You enter the escape capsule, press the big red button and escape the dying ship.")
        else:
            print("No idea what that means.")
        
def dead(why):
    print(why, "You are dead. Good job!")
    exit(0)

room_start()