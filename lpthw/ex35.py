from sys import exit

def gold_room():
    print("This room is full of gold\nHow much do you take?")
    
    how_much = int(input('> '))
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
        
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How you gonna shift it?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("No idea what that means.")
            
def cthulhu_room():
    print("Helloooooo! Cthulhu alert!")
    print("He, it, whatever, stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()
        
def dead(why):
    print(why, "Good job!")
    exit(0)
    
def start():
    print("You're in a dark room.")
    print("There are doors to Right and Left.")
    print("Which do you take?")
    
    choice = input("> ")
    
    if "left" in choice:
        bear_room()
    elif "right" in choice:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
start()