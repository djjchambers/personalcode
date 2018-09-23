from room import Room
from item import Item
from character import Character, Enemy, Friend
from random import randint

SCORE = 0
TREASURE = 0
backpack = []
DEFEATED = 0

kitchen = Room('Kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room('Dining Hall')
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room('Ballroom')
ballroom.set_description("A vast room with a shiny womble statue.")

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

# Add Enemy

dave = Enemy('Dave', 'A smelly zombie')
dave.set_weakness('cheese')
dining_hall.set_character(dave)
dave.set_money(randint(0, 10))

peter = Enemy('Peter', 'A giant squid')
peter.set_weakness('spatula')
kitchen.set_character(peter)
peter.set_money(randint(0,10))

zebulon = Enemy('Zebulon', 'a sentient gas cloud')
zebulon.set_weakness('dustbuster')
ballroom.set_character(zebulon)
zebulon.set_money(randint(0,5))

# Add new character

catrina = Friend("Catrina", "A friendly skellington")
kitchen.set_character(catrina)
catrina.set_money(randint(0, 10))
catrina.set_conversation("Wotcher, chuck")

# Add items

cheese = Item('cheese')
cheese.set_description('a lethal-looking wedge of sharp cheddar')
kitchen.set_item(cheese)

dustbuster = Item('dustbuster')
dustbuster.set_description('A handy-looking portable vacuum-cleaner')
ballroom.set_item(dustbuster)

spatula = Item('spatula')
spatula.set_description('a mean-looking wooden fish-slice')
dining_hall.set_item(spatula)

current_room = kitchen

game_over = False
dead = False

while game_over == False:

    # UPDATE
    print('\n')
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
    item = current_room.get_item()
    if item is not None:
        item.describe()
    
    # INPUT
    command = input('> ')

    if command in["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to inhabitant if there is one
        if inhabitant:
            inhabitant.talk()
    elif command == "steal":
        if inhabitant:
            spoils = randint(0, 3)
            if inhabitant.money < spoils:
                spoils = inhabitant.money
            if inhabitant.money > 0:
                if spoils == 0:
                    print(inhabitant.name + " shifts and you quickly withdraw an empty hand...")
                else:
                    inhabitant.set_money(inhabitant.money - spoils)
                    print("Stealthy! You nicked {} gold coins!".format(spoils))
                    TREASURE += spoils
                    print("You now have {} gold.".format(TREASURE))
            else:
                print(inhabitant.name + " is broke!")
        else:
            print("There's nobody here to steal from!")
    elif command == "fight":
        # Fight with inhabitant if there is one
        print("What will you fight with?")
        fight_with = input()
        if fight_with in backpack:
            if inhabitant:
                if isinstance(inhabitant, Enemy):
                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win
                        SCORE += 1
                        DEFEATED += 1
                        print("You killed " + inhabitant.name)
                        print("Your score went up to {0} points!".format(SCORE))
                        print("Total kills = {}".format(DEFEATED))
                        current_room.set_character(None)
                        if DEFEATED == 2:
                            game_over = True
                    else:
                        # What happens if you lose
                        print("You died!")
                        dead = True
                        game_over = True
                elif isinstance(inhabitant, Friend):
                    print("Back off, buster!")
        else:
            print("You aren't carrying: " + fight_with)
    elif command == "take":
        print("What do you want to take?")
        taking = input()
        if taking == item.get_name():
            print('You take the {}'.format(item.get_name()))
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("You can't see that here.")
    elif command == "inv":
        print("You are carrying:")
        for element in backpack:
            print(element)
    else:
        print("Invalid command!")
    
if dead == True:
    print("YOU ARE DEAD!")
elif dead == False:
    print("You defeated 5 enemies! YOU WIN!")